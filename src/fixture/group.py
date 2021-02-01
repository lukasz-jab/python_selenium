class GroupHelper:
    def __init__(self, app):
        self.app = app

    def modify_first_group(self, group):
        wd = self.app.wd
        self.app.navigation.open_groups()
        #wd.find_element_by_css_selector("div#content input[name='selected[]']").click()
        wd.find_element_by_css_selector("div#content input[name = edit]").click()
        self.fill_group_form(group)
        self.submit_group_form(wd)
        self.app.navigation.return_to_groups()


    def delete_first_group(self):
        wd = self.app.wd
        self.app.navigation.open_groups()
        self.select_first_group()
        wd.find_element_by_css_selector("div#content input[name='delete']").click()
        self.app.is_alert_present()
        self.app.navigation.return_to_groups()


    def create(self, group):
        wd = self.app.wd
        self.app.navigation.open_groups()
        # init group creation
        wd.find_element_by_css_selector("input[name = new]").click()
        self.fill_group_form(group)
        self.submit_group_form(wd)
        self.app.navigation.return_to_groups()


    def fill_group_form(self, group):
        self.change_field_value("input[name = group_name]", group.name)
        self.change_field_value("textarea[name = group_header]", group.header)
        self.change_field_value("textarea[name = group_footer]", group.footer)

    def change_field_value(self, locator, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_css_selector(locator).click()
            wd.find_element_by_css_selector(locator).clear()
            wd.find_element_by_css_selector(locator).send_keys(text)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div#content input[name='selected[]']").click()


    def submit_group_form(self, wd):
        wd.find_element_by_css_selector("div#content input[type=submit]").click()