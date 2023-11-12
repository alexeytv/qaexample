from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class PersonalPage(BasePage):
    PAGE_URL = Links.ACCOUNT_PAGE

    FIRSTNAME_FIELD = ("xpath", "//input[@name='account_first_name']")
    LASTNAME_FIELD = ("xpath", "//input[@name='account_last_name']")
    SUBMIT_BUTTON = ("xpath", "//button[@name='save_account_details']")
    new_last_name = ""
    new_first_name = ""

    def change_first_name(self, new_name):
        first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRSTNAME_FIELD))
        first_name_field.clear()
        assert first_name_field.get_attribute("value") == "", "There is text"
        first_name_field.send_keys(new_name)
        self.new_first_name = new_name

    def change_last_name(self, new_name):
        last_name_field = self.wait.until(EC.element_to_be_clickable(self.LASTNAME_FIELD))
        last_name_field.clear()
        assert last_name_field.get_attribute("value") == "", "There is text"
        last_name_field.send_keys(new_name)
        self.new_last_name = new_name

    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def is_changes_saved(self):
        self.wait.until(EC.text_to_be_present_in_element(self.FIRSTNAME_FIELD, self.new_first_name))
        self.wait.until(EC.text_to_be_present_in_element(self.LASTNAME_FIELD, self.new_last_name))
