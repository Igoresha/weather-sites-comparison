from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver, page_url):
        self.driver = driver
        self.base_url = page_url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message="Can't find element by locator {}".format(locator))

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def print_forecast_results(self, city_name, date, sinoptik_temp, dark_sky_temp):
        print("Sinoptik, city - {0}, date - {1}, forecast temp - min = {2}, max = {3}".
              format(city_name, date, str(sinoptik_temp[0]), str(sinoptik_temp[1])))
        print("Dark Sky, city - {0}, date - {1}, forecast temp - min = {2}, max = {3}".
              format(city_name, date, str(dark_sky_temp[0]), str(dark_sky_temp[1])))
