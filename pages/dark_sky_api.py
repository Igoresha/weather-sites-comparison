import requests
import time


class DarkSkyApi:

    odessa_city = "46.47747,30.73262"
    kiev_city = "50.45466, 30.5238"
    lviv_city = "49.83826, 24.02324"

    api_key = "d6ff02ed4dd4df15ce56e0ae9108dd8b"

    def get_daily_city_min_max_temp_for(self, day, city_coordinates):
        requested_days = {"second_day": 24*60*60, "third_day": 48*60*60, "fourth_day": 72*60*60}
        gmt_plus_2_hours = 2 * 60 * 60
        date_timestamp = int(time.time()) + gmt_plus_2_hours + requested_days[day]
        url = "https://api.darksky.net/forecast/{}/{},{}".format(self.api_key, city_coordinates, date_timestamp)
        payload = {'exclude': 'currently,flags,minutely,hourly,alerts',
                   'units': 'auto'}
        response = requests.get(url, params=payload)
        daily_dict = response.json()["daily"]
        data_list = daily_dict["data"]
        daily_forecast_dict = data_list[0]
        min_temp = int(round(daily_forecast_dict["temperatureMin"]))
        max_temp = int(round(daily_forecast_dict["temperatureMax"]))
        min_max_temp = [min_temp, max_temp]
        return min_max_temp

    def get_odessa_second_day_min_max_temp(self):
        return self.get_daily_city_min_max_temp_for("second_day", self.odessa_city)

    def get_odessa_third_day_min_max_temp(self):
        return self.get_daily_city_min_max_temp_for("third_day", self.odessa_city)

    def get_odessa_fourth_day_min_max_temp(self):
        return self.get_daily_city_min_max_temp_for("fourth_day", self.odessa_city)

    def get_kiev_second_day_min_max_temp(self):
        return self.get_daily_city_min_max_temp_for("second_day", self.kiev_city)

    def get_kiev_third_day_min_max_temp(self):
        return self.get_daily_city_min_max_temp_for("third_day", self.kiev_city)

    def get_kiev_fourth_day_min_max_temp(self):
        return self.get_daily_city_min_max_temp_for("fourth_day", self.kiev_city)

    def get_lviv_second_day_min_max_temp(self):
        return self.get_daily_city_min_max_temp_for("second_day", self.lviv_city)

    def get_lviv_third_day_min_max_temp(self):
        return self.get_daily_city_min_max_temp_for("third_day", self.lviv_city)

    def get_lviv_fourth_day_min_max_temp(self):
        return self.get_daily_city_min_max_temp_for("fourth_day", self.lviv_city)
