class ContactHelper:
    def __init__(self, app):
        self.app = app

    def modify_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']//a[contains(@href, 'edit.php')]").click()
        wd.find_element_by_css_selector("input[name=firstname]").send_keys(contact.firstname)
        wd.find_element_by_css_selector("input[name=lastname]").send_keys(contact.lastname)
        wd.find_element_by_css_selector("textarea[name=address]").send_keys(contact.address)
        wd.find_element_by_css_selector("input[name=mobile]").send_keys(contact.mobile)
        wd.find_element_by_css_selector("textarea[name=notes]").send_keys(contact.notes)
        self.submit_form()

    def submit_form(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div#content input[type=submit]").click()
        # self.wd.execute_script("arguments[0].click()", self.wd.find_element_by_css_selector("input[type=submit][name=submit]"))

    def delete(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("table#maintable input[name='selected[]']").click()
        # Dont know it will pass to application below 9.0 version)
        wd.find_element_by_xpath("//form[@name='MainForm']//input[@type='button' and @onclick='DeleteSel()']").click()
        self.app.is_alert_present()

    def fill_form(self, contact):
        wd = self.app.wd
        self.app.navigation.open_contacts()
        wd.find_element_by_css_selector("input[name=firstname]").send_keys(contact.firstname)
        wd.find_element_by_css_selector("input[name=lastname]").send_keys(contact.lastname)
        wd.find_element_by_css_selector("textarea[name=address]").send_keys(contact.address)
        wd.find_element_by_css_selector("input[name=mobile]").send_keys(contact.mobile)
        wd.find_element_by_css_selector("textarea[name=notes]").send_keys(contact.notes)
        self.submit_form()