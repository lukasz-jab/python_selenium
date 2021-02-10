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
        Element = wd.find_element_by_css_selector("input[type=submit]")
        wd.execute_script("arguments[0].scrollIntoView();", Element);
        Element.click()


    def delete(self):
        self.delete_by_index(0)

    def create(self, contact):
        wd = self.app.wd
        self.app.navigation.open_contacts()
        self.fill_form(contact)
        self.submit()
        self.contact_cache = None

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

    contact_cache = None

    def get_contacs_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.navigation.open_home()
            self.contact_cache = []
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
                self.contact_cache.append(Contact(id=c_id, firstname=c_firstnames[i]))
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