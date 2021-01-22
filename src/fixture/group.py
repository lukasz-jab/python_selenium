class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.app.navigation.open_groups()
        # init group creation
        wd.find_element_by_css_selector("input[name = new]").click()
        # fill group form
        wd.find_element_by_css_selector("input[name = group_name]").click()
        wd.find_element_by_css_selector("input[name = group_name]").clear()
        wd.find_element_by_css_selector("input[name = group_name]").send_keys(group.name)
        wd.find_element_by_css_selector("textarea[name = group_header]").click()
        wd.find_element_by_css_selector("textarea[name = group_header]").clear()
        wd.find_element_by_css_selector("textarea[name = group_header]").send_keys(group.header)
        wd.find_element_by_css_selector("textarea[name = group_footer]").click()
        wd.find_element_by_css_selector("textarea[name = group_footer]").clear()
        wd.find_element_by_css_selector("textarea[name = group_footer]").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_css_selector("input[name = submit]").click()
        self.app.navigation.return_to_groups()


    def delete(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div#content input[name='selected[]']").click()
        wd.find_element_by_css_selector("div#content input[name='delete']").click()
        self.app.is_alert_present()

