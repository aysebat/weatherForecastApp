import requests

apikey="4429faaaa08bd6135bd6b3c567c46811"

class Weather:



    def __init__(self, apikey, city, lat=None, lon=None):
        url = f"https: // api.openweathermap.org / data / 2.5 / weather?q = {city} & appid = {apikey}"
        self.apikey = apikey
        self.city = city
        self.lat = lat
        self.lon = lon

    def next_12h(self):
        pass

    def next_12h_simple(self):
        pass


