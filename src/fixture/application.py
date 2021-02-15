from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

from src.fixture.contact import ContactHelper
from src.fixture.group import GroupHelper
from src.fixture.navigation import NavigationHelper
from src.fixture.session import SessionHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.base_url = base_url
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.navigation = NavigationHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert().accept()
        except NoAlertPresentException as e:
            return False
        return True

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
