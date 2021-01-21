import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from contact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(10)

    def test_add_contact(self):
        self.login("admin", "secret")
        self.fill_contact_form(Contact("lukasz", "jab", "polska", "555555", "notes notes notes"))
        self.logout()

    def login(self, username, password):
        wd = self.wd
        wd.get("http://127.0.0.1/addressbook/index.php")
        wd.find_element_by_css_selector("input[name=user]").send_keys(username)
        wd.find_element_by_css_selector("input[name=pass]").send_keys(password)
        wd.find_element_by_css_selector("input[type=submit][value=Login]").click()

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
        wd.find_element_by_xpath("//a[@onclick='document.logout.submit();']")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()
