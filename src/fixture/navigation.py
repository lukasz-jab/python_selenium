from selenium.webdriver.common.by import By


class NavigationHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href, 'group.php')]").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://127.0.0.1/addressbook/index.php")

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href,'edit.php')]").click()
        # I have app in version 9.0
        if (self.app.is_element_present(By.CSS_SELECTOR, ("input[type=submit][name=quickadd]"))):
            wd.find_element_by_css_selector("input[type=submit][name=quickadd]").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//a[contains(@href, 'group.php')])[2]").click()

