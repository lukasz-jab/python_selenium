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
        wd = self.wd
        self.login(wd, "admin", "secret")
        self.open_contact_page(wd)
        self.fill_contact_form(wd, Contact("lukasz", "jab", "polska", "555555", "notes notes notes"))
        self.submit_contact_form(wd)
        self.logout(wd)

    def login(self, wd, username, password):
        self.wd.get("http://127.0.0.1/addressbook/index.php")
        self.wd.find_element_by_css_selector("input[name=user]").send_keys(username)
        self.wd.find_element_by_css_selector("input[name=pass]").send_keys(password)
        self.wd.find_element_by_css_selector("input[type=submit][value=Login]").click()

    def open_contact_page(self, wd):
        self.wd.find_element_by_xpath("//a[contains(@href,'edit.php')]").click()
        # I have app in version 9.0
        if (self.is_element_present(By.CSS_SELECTOR, ("input[type=submit][name=quickadd]"))):
            self.wd.find_element_by_css_selector("input[type=submit][name=quickadd]").click()

    def fill_contact_form(self, wd, contact):
        self.wd.find_element_by_css_selector("input[name=firstname]").send_keys(contact.firstname)
        self.wd.find_element_by_css_selector("input[name=lastname]").send_keys(contact.lastname)
        self.wd.find_element_by_css_selector("textarea[name=address]").send_keys(contact.address)
        self.wd.find_element_by_css_selector("input[name=mobile]").send_keys(contact.mobile)
        self.wd.find_element_by_css_selector("textarea[name=notes]").send_keys(contact.notes)

    def submit_contact_form(self, wd):
        self.wd.find_element_by_css_selector("input[type=submit][name=submit]").click()
        # self.wd.execute_script("arguments[0].click()", self.wd.find_element_by_css_selector("input[type=submit][name=submit]"))

    def logout(self, wd):
        self.wd.find_element_by_xpath("//a[@onclick='document.logout.submit();']")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()
