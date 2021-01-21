from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(10)


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

    def open_contact_page(self):
        wd = self.wd
        wd.find_element_by_xpath("//a[contains(@href,'edit.php')]").click()
        # I have app in version 9.0
        if (self.is_element_present(By.CSS_SELECTOR, ("input[type=submit][name=quickadd]"))):
            wd.find_element_by_css_selector("input[type=submit][name=quickadd]").click()

    def fill_contact_form(self, contact):
        wd = self.wd
        self.open_contact_page()
        wd.find_element_by_css_selector("input[name=firstname]").send_keys(contact.firstname)
        wd.find_element_by_css_selector("input[name=lastname]").send_keys(contact.lastname)
        wd.find_element_by_css_selector("textarea[name=address]").send_keys(contact.address)
        wd.find_element_by_css_selector("input[name=mobile]").send_keys(contact.mobile)
        wd.find_element_by_css_selector("textarea[name=notes]").send_keys(contact.notes)
        self.submit_contact_form()

    def submit_contact_form(self):
        wd = self.wd
        wd.find_element_by_css_selector("input[type=submit][name=submit]").click()
        # self.wd.execute_script("arguments[0].click()", self.wd.find_element_by_css_selector("input[type=submit][name=submit]"))


    def logout(self):
        wd = self.wd
        wd.find_element_by_xpath("//a[@onclick='document.logout.submit();']").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_xpath("(//a[contains(@href, 'group.php')])[2]").click()


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
