class ContactHelper:
    def __init__(self, app):
        self.app = app

    def fill_form(self, contact):
        wd = self.app.wd
        self.app.navigation.open_contact_page()
        wd.find_element_by_css_selector("input[name=firstname]").send_keys(contact.firstname)
        wd.find_element_by_css_selector("input[name=lastname]").send_keys(contact.lastname)
        wd.find_element_by_css_selector("textarea[name=address]").send_keys(contact.address)
        wd.find_element_by_css_selector("input[name=mobile]").send_keys(contact.mobile)
        wd.find_element_by_css_selector("textarea[name=notes]").send_keys(contact.notes)
        self.submit_form()

    def submit_form(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[type=submit][name=submit]").click()
        # self.wd.execute_script("arguments[0].click()", self.wd.find_element_by_css_selector("input[type=submit][name=submit]"))
