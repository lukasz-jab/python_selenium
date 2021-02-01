from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.navigation.open_home()
        wd.find_element_by_css_selector("input[name = user]").send_keys(username)
        wd.find_element_by_css_selector("input[name = pass]").send_keys(password)
        wd.find_element_by_css_selector("input[type = submit][value = Login]").click()

    def logout(self):
        wd = self.app.wd
        # wd.find_element_by_xpath("//a[@onclick='document.logout.submit();']").click()
        #added for univeral language version - in polish Usuń-delete
        WebDriverWait(wd, 3).until(EC.element_to_be_clickable((By.XPATH, "//a[@onclick='document.logout.submit();']"))).click()


    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//a[contains(@onclick, 'document.logout.submit();')]")) > 0


    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_css_selector("div#container div#top b").text == "(" + username + ")"

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)



