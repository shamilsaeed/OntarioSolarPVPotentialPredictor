from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather
from datetime import datetime
from datetime import timedelta
from .core import *

API_KEY = 'ec483638551ba840c5e3cf99ad694d1e'

# Synchronous way
darksky = DarkSky(API_KEY)

date_time_str = '2017-07-01 00:00:00'
date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

latitude = 43.581381
longitude = -79.647606

# This will do from 2017-07-01 to 2017-07-05 both inclusive
amount_of_days_from_initial_date = 5

for day_to_add in range(amount_of_days_from_initial_date):
    date_to_use = date_time_obj + timedelta(days=day_to_add)

    forecast = darksky.get_time_machine_forecast(
        latitude, longitude,
        date_to_use,
        extend=True,
        lang=languages.ENGLISH,
        units=units.CA,
        exclude=[weather.CURRENTLY, weather.DAILY, weather.FLAGS]
    )

    print(date_to_use)
    # This goes from 9 am to 5 pm, if it is until 4pm replace 18 by 17
    for hour_item in forecast.hourly.data[9:18]:
        temperature = hour_item.temperature  # float
        uv_index = hour_item.uv_index  # int
        wind_speed = hour_item.wind_speed  # float
        cloud_cover = hour_item.cloud_cover  # float
        precip_intensity = hour_item.precip_intensity  # float

        print(str(hour_item.temperature) + '***' + str(hour_item.time))
