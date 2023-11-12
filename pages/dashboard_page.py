from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE

    ANKETA_LINK = ("xpath", "//link[text()='Анкета']")

    def click_anketa_link(self):
        self.wait.until(EC.element_to_be_clickable(self.ANKETA_LINK)).click()