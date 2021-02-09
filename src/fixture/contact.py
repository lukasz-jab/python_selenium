from src.model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def modify(self, contact):
        wd = self.app.wd
        self.app.navigation.open_home()
        wd.find_element_by_xpath("//table[@id='maintable']//a[contains(@href, 'edit.php')]").click()
        self.fill_form(contact)
        self.submit()

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div#content input[type=submit]").click()
        # self.wd.execute_script("arguments[0].click()", self.wd.find_element_by_css_selector("input[type=submit][name=submit]"))

    def delete(self):
        wd = self.app.wd
        self.app.navigation.open_home()
        wd.find_element_by_css_selector("table#maintable input[name='selected[]']").click()
        # Dont know it will pass to application below 9.0 version)
        wd.find_element_by_xpath("//form[@name='MainForm']//input[@type='button' and @onclick='DeleteSel()']").click()
        self.app.is_alert_present()

    def create(self, contact):
        wd = self.app.wd
        self.app.navigation.open_contacts()
        self.fill_form(contact)
        self.submit()

    def fill_form(self, contact):
        self.change_field_value("input[name=firstname]", contact.firstname)
        self.change_field_value("input[name=lastname]", contact.lastname)
        self.change_field_value("textarea[name=address]", contact.address)
        self.change_field_value("input[name=mobile]", contact.mobile)
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

    def get_contacs_list(self):
        wd = self.app.wd
        self.app.navigation.open_home()
        contacts = []
        edit_links = []
        c_firstnames = []
        web_elements_contact = wd.find_elements_by_css_selector("table#maintable input[name='selected[]']")
        for web_el in web_elements_contact:
            edit_links.append(web_el.get_attribute("id"))
        for link in edit_links:
            wd.find_element_by_css_selector("a[href='edit.php?id=" + link + "']").click()
            c_firstnames.append(wd.find_element_by_css_selector("input[name=firstname]").get_attribute("value"))
            self.app.navigation.open_home()
        i = 0
        for c_id in edit_links:
            contacts.append(Contact(id=c_id, firstname=c_firstnames[i]))
            i = i + 1
        return contacts
