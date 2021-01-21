from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(10)


    def logout(self):
        wd = self.wd
        wd.find_element_by_xpath("//a[@onclick='document.logout.submit();']").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_xpath("(//a[contains(@href, 'group.php')])[2]").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
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
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_xpath("//a[contains(@href, 'group.php')]").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_css_selector("input[name = user]").send_keys(username)
        wd.find_element_by_css_selector("input[name = pass]").send_keys(password)
        wd.find_element_by_css_selector("input[type = submit][value = Login]").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://127.0.0.1/addressbook/index.php")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True


    def destroy(self):
        self.wd.quit()