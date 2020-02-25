from base_page import BasePage
from selenium.webdriver.common.by import By
import re
import datetime
import time


class SinoptikBasePageLocators:
    SINOPTIK_SEARCH_FIELD = (By.XPATH, "//input[@id='search_city']")
    SINOPTIK_SEARCH_BUTTON = (By.XPATH, "//input[@class='search_city-submit']")

    def sinoptok_date_and_city_base_locator(day_number):
        return By.XPATH, "//div[@id='bd{}']/p/a".format(day_number)
    SINOPTIK_SECOND_DAY_DATE = sinoptok_date_and_city_base_locator("2")
    SINOPTIK_THIRD_DAY_DATE = sinoptok_date_and_city_base_locator("3")
    SINOPTIK_FOURTH_DAY_DATE = sinoptok_date_and_city_base_locator("4")

    def sinoptok_min_max_temp_locator(day_number, temp):
        return By.XPATH, "//div[@id='bd{0}']//div[@class='temperature']/div[@class='{1}']/span".format(day_number, temp)
    SINOPTIK_SECOND_DAY_MIN_TEMP = sinoptok_min_max_temp_locator("2", "min")
    SINOPTIK_SECOND_DAY_MAX_TEMP = sinoptok_min_max_temp_locator("2", "max")
    SINOPTIK_THIRD_DAY_MIN_TEMP = sinoptok_min_max_temp_locator("3", "min")
    SINOPTIK_THIRD_DAY_MAX_TEMP = sinoptok_min_max_temp_locator("3", "max")
    SINOPTIK_FOURTH_DAY_MIN_TEMP = sinoptok_min_max_temp_locator("4", "min")
    SINOPTIK_FOURTH_DAY_MAX_TEMP = sinoptok_min_max_temp_locator("4", "max")


class SinoptikBasePage(BasePage, SinoptikBasePageLocators):

    def enter_word_in_search_bar(self, word):
        search_field = self.find_element(self.SINOPTIK_SEARCH_FIELD, time=2)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(self.SINOPTIK_SEARCH_BUTTON, time=2).click()

    def _get_date(self, date_locator):
        time.sleep(1)
        raw_date = self.find_element(date_locator, time=2).get_attribute("data-link")
        date_object = re.search(r'\d{4}-\d{2}-\d{2}', raw_date)
        string_date = datetime.datetime.strptime(date_object.group(), '%Y-%m-%d').date()
        return string_date

    def _get_min_max_temp(self, min_locator, max_locator):
        min_temp = int(self.find_element(min_locator, time=2).text.encode('ascii', 'ignore'))
        max_temp = int(self.find_element(max_locator, time=2).text.encode('ascii', 'ignore'))
        min_max_temp = [min_temp, max_temp]
        return min_max_temp

    def get_second_day_date(self):
        return self._get_date(self.SINOPTIK_SECOND_DAY_DATE)

    def get_third_day_date(self):
        return self._get_date(self.SINOPTIK_THIRD_DAY_DATE)

    def get_fourth_day_date(self):
        return self._get_date(self.SINOPTIK_FOURTH_DAY_DATE)

    def get_second_day_min_max_temp(self):
        return self._get_min_max_temp(self.SINOPTIK_SECOND_DAY_MIN_TEMP, self.SINOPTIK_SECOND_DAY_MAX_TEMP)

    def get_third_day_min_max_temp(self):
        return self._get_min_max_temp(self.SINOPTIK_THIRD_DAY_MIN_TEMP, self.SINOPTIK_THIRD_DAY_MAX_TEMP)

    def get_fourth_day_min_max_temp(self):
        return self._get_min_max_temp(self.SINOPTIK_FOURTH_DAY_MIN_TEMP, self.SINOPTIK_FOURTH_DAY_MAX_TEMP)
