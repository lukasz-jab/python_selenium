import re

from src.model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def modify(self, index, contact):
        wd = self.app.wd
        self.app.navigation.open_home()
        wd.find_elements_by_xpath("//table[@id='maintable']//a[contains(@href, 'edit.php')]")[index].click()
        self.fill_form(contact)
        self.submit()
        self.contact_cache = None

    def submit(self):
        wd = self.app.wd
        # chromedriver 88 cannot find but can click css selector ("input[type=submit]")
        element = wd.find_element_by_xpath("//input[@type='submit']")
        wd.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        self.app.navigation.open_home()

    def delete(self):
        self.delete_by_index(0)

    def create(self, contact):
        self.app.navigation.open_contacts()
        self.fill_form(contact)
        self.submit()
        self.contact_cache = None

    def fill_form(self, contact):
        self.change_field_value("input[name=firstname]", contact.firstname)
        self.change_field_value("input[name=lastname]", contact.lastname)
        self.change_field_value("textarea[name=address]", contact.address)
        self.change_field_value("input[name=mobile]", contact.mobilephone)
        self.change_field_value("textarea[name=notes]", contact.notes)
        self.submit()

    def change_field_value(self, locator, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_css_selector(locator).clear()
            wd.find_element_by_css_selector(locator).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_home()
        return len(wd.find_elements_by_css_selector("table#maintable input[name='selected[]']"))

    contact_cache = None

    def get_contacs_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.navigation.open_home()
            self.contact_cache = []
            edit_links = []
            c_firstnames = []
            c_lastnames = []
            c_all_phones = []
            c_all_emails = []
            c_address = []
            web_elements_contact = wd.find_elements_by_css_selector("table#maintable input[name='selected[]']")
            for web_el in web_elements_contact:
                edit_links.append(web_el.get_attribute("id"))
                c_all_phones.append(web_el.find_element_by_xpath("./../following-sibling::td[5]").text)
                c_all_emails.append(web_el.find_element_by_xpath("./../following-sibling::td[4]").text)
                c_address.append(web_el.find_element_by_xpath("./../following-sibling::td[3]").text)
            for link in edit_links:
                wd.find_element_by_css_selector("a[href='edit.php?id=" + link + "']").click()
                c_firstnames.append(wd.find_element_by_css_selector("input[name=firstname]").get_attribute("value"))
                c_lastnames.append(wd.find_element_by_css_selector("input[name=lastname]").get_attribute("value"))
                self.app.navigation.open_home()
            i = 0
            for c_id in edit_links:
                phones = c_all_phones[i]
                emails = c_all_emails[i]
                address = c_address[i]
                self.contact_cache.append(Contact(id=c_id, firstname=c_firstnames[i], lastname=c_lastnames[i],
                                                  all_phones_from_home_page=phones, all_emails=emails, address=address))
                i = i + 1
        return list(self.contact_cache)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home()
        wd.find_elements_by_css_selector("table#maintable input[name='selected[]']")[index].click()
        # Dont know it will pass to application below 9.0 version)
        wd.find_element_by_xpath("//form[@name='MainForm']//input[@type='button' and @onclick='DeleteSel()']").click()
        self.app.is_alert_present()
        self.contact_cache = None

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home()
        wd.find_element_by_css_selector("a[href='view.php?id=" + str(index) + "']").click()

    def open_contact_edit_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home()
        wd.find_element_by_css_selector("a[href='edit.php?id=" + str(index) + "']").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_by_index(index)
        id = wd.find_element_by_css_selector("input[name=id]").get_attribute("value")
        first_name = wd.find_element_by_css_selector("input[name=firstname]").get_attribute("value")
        last_name = wd.find_element_by_css_selector("input[name=lastname]").get_attribute("value")
        home_phone = wd.find_element_by_css_selector("input[name=home]").get_attribute("value")
        mobile_phone = wd.find_element_by_css_selector("input[name=mobile]").get_attribute("value")
        work_phone = wd.find_element_by_css_selector("input[name=work]").get_attribute("value")
        email_1 = wd.find_element_by_css_selector("input[name=email]").get_attribute("value")
        email_2 = wd.find_element_by_css_selector("input[name=email2]").get_attribute("value")
        email_3 = wd.find_element_by_css_selector("input[name=email3]").get_attribute("value")
        address = wd.find_element_by_css_selector("textarea[name=address]").get_attribute("value")
        notes = wd.find_element_by_css_selector("textarea[name=notes]").get_attribute("value")
        fax_phone = wd.find_element_by_css_selector("input[name=fax]").get_attribute("value")
        return Contact(id=id, firstname=first_name, lastname=last_name, homephone=home_phone, mobilephone=mobile_phone,
                       workphone=work_phone, email_1=email_1, email_2=email_2, email_3=email_3,
                       address=address, notes=notes)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_css_selector("div#content").text
        homephone = re.findall("H: (.*)", text)
        mobilephone = re.findall("M: (.*)", text)
        workphone = re.findall("W: (.*)", text)
        # faxphone = re.findall("F: (.*)", text)
        email_1 = wd.find_element_by_css_selector("a[href^='mailto']")
        allphones = homephone + mobilephone + workphone
        return Contact(all_phones_from_home_page="\n".join([str(elem) for elem in allphones]), email_1=email_1)

    def delete_by_id(self, id):
        wd = self.app.wd
        self.app.navigation.open_home()
        wd.find_element_by_css_selector("table#maintable input[value='" + str(id) + "']").click()
        # Dont know it will pass to application below 9.0 version)
        wd.find_element_by_xpath("//form[@name='MainForm']//input[@type='button' and @onclick='DeleteSel()']").click()
        self.app.is_alert_present()
        self.contact_cache = None

    def modify_by_id(self, id, contact):
        wd = self.app.wd
        self.app.navigation.open_home()
        wd.find_element_by_xpath("//table[@id='maintable']//a[contains(@href, 'edit.php?id=%s')]" % id).click()
        self.fill_form(contact)
        self.submit()
        self.contact_cache = None
