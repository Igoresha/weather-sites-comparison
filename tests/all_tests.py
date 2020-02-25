# -*- coding: utf-8 -*-
from pages.sinoptik_pages import SinoptikBasePage
from pages.dark_sky_api import DarkSkyApi


def test_compare_odessa_second_day_forecast_on_two_weather_sites(browser):
    sinoptik_base_page = SinoptikBasePage(browser, "https://sinoptik.ua/")
    dark_sky_api = DarkSkyApi()
    sinoptik_base_page.go_to_site()
    sinoptik_base_page.enter_word_in_search_bar(u"Одесса")
    sinoptik_base_page.click_on_the_search_button()

    sinoptik_date = sinoptik_base_page.get_second_day_date()
    sinoptik_temp = sinoptik_base_page.get_second_day_min_max_temp()
    dark_sky_temp = dark_sky_api.get_odessa_second_day_min_max_temp()
    sinoptik_base_page.print_forecast_results("Odessa", sinoptik_date,
                                              sinoptik_temp, dark_sky_temp)
    assert sinoptik_temp == dark_sky_temp, 'Temperature is different on Sinoptik and Dark Sky'


def test_compare_odessa_third_day_forecast_on_two_weather_sites(browser):
    sinoptik_base_page = SinoptikBasePage(browser, "https://sinoptik.ua/")
    dark_sky_api = DarkSkyApi()
    sinoptik_base_page.go_to_site()
    sinoptik_base_page.enter_word_in_search_bar(u"Одесса")
    sinoptik_base_page.click_on_the_search_button()

    sinoptik_date = sinoptik_base_page.get_third_day_date()
    sinoptik_temp = sinoptik_base_page.get_third_day_min_max_temp()
    dark_sky_temp = dark_sky_api.get_odessa_third_day_min_max_temp()
    sinoptik_base_page.print_forecast_results("Odessa", sinoptik_date,
                                              sinoptik_temp, dark_sky_temp)
    assert sinoptik_temp == dark_sky_temp, 'Temperature is different on Sinoptik and Dark Sky'


def test_compare_odessa_fourth_day_forecast_on_two_weather_sites(browser):
    sinoptik_base_page = SinoptikBasePage(browser, "https://sinoptik.ua/")
    dark_sky_api = DarkSkyApi()
    sinoptik_base_page.go_to_site()
    sinoptik_base_page.enter_word_in_search_bar(u"Одесса")
    sinoptik_base_page.click_on_the_search_button()

    sinoptik_date = sinoptik_base_page.get_fourth_day_date()
    sinoptik_temp = sinoptik_base_page.get_fourth_day_min_max_temp()
    dark_sky_temp = dark_sky_api.get_odessa_fourth_day_min_max_temp()
    sinoptik_base_page.print_forecast_results("Odessa", sinoptik_date,
                                              sinoptik_temp, dark_sky_temp)
    assert sinoptik_temp == dark_sky_temp, 'Temperature is different on Sinoptik and Dark Sky'


def test_compare_kiev_second_day_forecast_on_two_weather_sites(browser):
    sinoptik_base_page = SinoptikBasePage(browser, "https://sinoptik.ua/")
    dark_sky_api = DarkSkyApi()
    sinoptik_base_page.go_to_site()
    sinoptik_base_page.enter_word_in_search_bar(u"Киев")
    sinoptik_base_page.click_on_the_search_button()

    sinoptik_date = sinoptik_base_page.get_second_day_date()
    sinoptik_temp = sinoptik_base_page.get_second_day_min_max_temp()
    dark_sky_temp = dark_sky_api.get_kiev_second_day_min_max_temp()
    sinoptik_base_page.print_forecast_results("Kiev", sinoptik_date,
                                              sinoptik_temp, dark_sky_temp)
    assert sinoptik_temp == dark_sky_temp, 'Temperature is different on Sinoptik and Dark Sky'


def test_compare_kiev_third_day_forecast_on_two_weather_sites(browser):
    sinoptik_base_page = SinoptikBasePage(browser, "https://sinoptik.ua/")
    dark_sky_api = DarkSkyApi()
    sinoptik_base_page.go_to_site()
    sinoptik_base_page.enter_word_in_search_bar(u"Киев")
    sinoptik_base_page.click_on_the_search_button()

    sinoptik_date = sinoptik_base_page.get_third_day_date()
    sinoptik_temp = sinoptik_base_page.get_third_day_min_max_temp()
    dark_sky_temp = dark_sky_api.get_kiev_third_day_min_max_temp()
    sinoptik_base_page.print_forecast_results("Kiev", sinoptik_date,
                                              sinoptik_temp, dark_sky_temp)
    assert sinoptik_temp == dark_sky_temp, 'Temperature is different on Sinoptik and Dark Sky'


def test_compare_kiev_fourth_day_forecast_on_two_weather_sites(browser):
    sinoptik_base_page = SinoptikBasePage(browser, "https://sinoptik.ua/")
    dark_sky_api = DarkSkyApi()
    sinoptik_base_page.go_to_site()
    sinoptik_base_page.enter_word_in_search_bar(u"Киев")
    sinoptik_base_page.click_on_the_search_button()

    sinoptik_date = sinoptik_base_page.get_fourth_day_date()
    sinoptik_temp = sinoptik_base_page.get_fourth_day_min_max_temp()
    dark_sky_temp = dark_sky_api.get_kiev_fourth_day_min_max_temp()
    sinoptik_base_page.print_forecast_results("Kiev", sinoptik_date,
                                              sinoptik_temp, dark_sky_temp)
    assert sinoptik_temp == dark_sky_temp, 'Temperature is different on Sinoptik and Dark Sky'


def test_compare_lviv_second_day_forecast_on_two_weather_sites(browser):
    sinoptik_base_page = SinoptikBasePage(browser, "https://sinoptik.ua/")
    dark_sky_api = DarkSkyApi()
    sinoptik_base_page.go_to_site()
    sinoptik_base_page.enter_word_in_search_bar(u"Львов")
    sinoptik_base_page.click_on_the_search_button()

    sinoptik_date = sinoptik_base_page.get_second_day_date()
    sinoptik_temp = sinoptik_base_page.get_second_day_min_max_temp()
    dark_sky_temp = dark_sky_api.get_lviv_second_day_min_max_temp()
    sinoptik_base_page.print_forecast_results("Lviv", sinoptik_date,
                                              sinoptik_temp, dark_sky_temp)
    assert sinoptik_temp == dark_sky_temp, 'Temperature is different on Sinoptik and Dark Sky'


def test_compare_lviv_third_day_forecast_on_two_weather_sites(browser):
    sinoptik_base_page = SinoptikBasePage(browser, "https://sinoptik.ua/")
    dark_sky_api = DarkSkyApi()
    sinoptik_base_page.go_to_site()
    sinoptik_base_page.enter_word_in_search_bar(u"Львов")
    sinoptik_base_page.click_on_the_search_button()

    sinoptik_date = sinoptik_base_page.get_third_day_date()
    sinoptik_temp = sinoptik_base_page.get_third_day_min_max_temp()
    dark_sky_temp = dark_sky_api.get_lviv_third_day_min_max_temp()
    sinoptik_base_page.print_forecast_results("Lviv", sinoptik_date,
                                              sinoptik_temp, dark_sky_temp)
    assert sinoptik_temp == dark_sky_temp, 'Temperature is different on Sinoptik and Dark Sky'


def test_compare_lviv_fourth_day_forecast_on_two_weather_sites(browser):
    sinoptik_base_page = SinoptikBasePage(browser, "https://sinoptik.ua/")
    dark_sky_api = DarkSkyApi()
    sinoptik_base_page.go_to_site()
    sinoptik_base_page.enter_word_in_search_bar(u"Львов")
    sinoptik_base_page.click_on_the_search_button()

    sinoptik_date = sinoptik_base_page.get_fourth_day_date()
    sinoptik_temp = sinoptik_base_page.get_fourth_day_min_max_temp()
    dark_sky_temp = dark_sky_api.get_lviv_fourth_day_min_max_temp()
    sinoptik_base_page.print_forecast_results("Львов", sinoptik_date,
                                              sinoptik_temp, dark_sky_temp)
    assert sinoptik_temp == dark_sky_temp, 'Temperature is different on Sinoptik and Dark Sky'
