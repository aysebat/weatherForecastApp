import requests

apikey="4429faaaa08bd6135bd6b3c567c46811"

class Weather:

    def __init__(self, apikey=None, city=None, lat=None, lon=None):
        self.apikey = apikey
        self.city = city
        self.lat = lat
        self.lon = lon
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




    def next_12h(self):
        pass

    def next_12h_simple(self):
        pass


#weather = Weather(apikey=apikey, city="Roma")
weather = Weather(apikey=apikey, lat=4.1, lon=3.2)
print(weather.data)