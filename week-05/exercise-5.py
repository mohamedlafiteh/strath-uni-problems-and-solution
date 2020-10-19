import json


def read_json(file_name):
    with open(file_name, "r", encoding="utf-8") as fjson:
        data = json.load(fjson)
        return data


class Species:

    def __init__(self, code, airQualityIndex):
        self.code = code
        self.airQualityIndex = airQualityIndex

    def loadFromJson(self, jsonData):
        self.code = jsonData["code"]
        self.airQualityIndex = jsonData["airQualityIndex"]

    def __repr__(self):
        return f"The code is {self.code}, \n The air quality is {self.airQualityIndex}"


class Site:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.species = []

    def loadFromJson(self, jsonData):

        self.name = jsonData["name"]
        self.latitude = jsonData["latitude"]
        self.longitude = jsonData["longitude"]
        del self.species[:]
        for jsonSite in jsonData["species"]:
            species = Species(jsonSite["code"], jsonSite["airQualityIndex"])
            species.loadFromJson(jsonSite)
            self.species += [species]


def __repr__(self):
    return f"The name is {self.name}, \n The latitude is {self.latitude} \n  The longitude is {self.longitude}. \n The Species are {self.species}"


class LocalAuthority:
    def __init__(self, name):
        self.name = name
        self.sites = []

    def loadFromJson(self, jsonData):
        self.name = jsonData["name"]
        del self.sites[:]
        for jsonSite in jsonData["sites"]:
            site = Site(jsonSite["name"],
                        jsonSite["latitude"], jsonSite["longitude"])
            site.loadFromJson(jsonSite)
            self.sites += [site]

    def __repr__(self):
        return f"The name is {self.name}, \n The site list is {self.sites}"


if __name__ == "__main__":
    js_data = read_json("./AirQuality.json")
    data_m = {}
    for data in js_data:
        data_m.update(data)


authority = LocalAuthority(data_m["name"])
authority.loadFromJson(data_m)
