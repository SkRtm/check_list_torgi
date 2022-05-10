from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeOutException
from selenium.common.exceptions import NoSuchElementException


class BasePage():

    def __init__(self, browser, link):
        self.browser = browser
        self.link = link

    def open(self):
        self.browser.get(self.link)

    def get_element_wait(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((method, locator)))
        except TimeOutException:
            return False
        return True


