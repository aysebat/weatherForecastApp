import requests
from datetime import datetime

apikey = "4429faaaa08bd6135bd6b3c567c46811"
class Weather:
    """"
    Creates a Weather object getting apikey as input
    and either a city name or lat and lot coordinates.

    Package use example:
    # Create weather object using a city name:
    # The api key below is not guranteed to work.
    # Get your own api key from https://openweathermap.org
    #And wait a couple of hour the apikey to be activated

    >> apikey="4429faaaa08bd6135bd6b3c567c46811"
    >> weather1 = Weather(apikey=apikey, city="Roma")

    ##Using lattitude and longitude
    >>weather2 = Weather(apikey=apikey, lat=4.1, lon=3.2)

    ##get coplete for the weather data
    >>weather1.weather_data()
    """

    def __init__(self, apikey=None, city=None, lat=None, lon=None):
        self.apikey = apikey
        self.city = city
        self.lat = lat
        self.lon = lon
        try:
            if apikey:
                if city:
                    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"
                elif lat and lon:
                    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}"
                else:
                    raise TypeError("Provide either a city or lat and lon argument.")
            else:
                raise TypeError("Please! Provide a valid API key.")

            r = requests.get(url)
            self.data = r.json()
        except:
            raise ValueError(self.data["message"])

    def weather_data(self):
        return (datetime.fromtimestamp(self.data['dt']).isoformat(),
                self.data['main']['temp'],
                self.data['weather'][0]['description'])
