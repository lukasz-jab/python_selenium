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
            wd.find_element_by_css_selector(locator).send_keys(text)


    def count(self):
        wd = self.app.wd
        self.app.navigation.open_home()
        return len(wd.find_elements_by_css_selector("table#maintable input[name='selected[]']"))