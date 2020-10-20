import json


def read_json(file_name):
    with open(file_name, "r", encoding="utf-8") as fjson:
        data = json.load(fjson)
        return data


class Species:

    def __init__(self):
        self.code = ""
        self.airQualityIndex = 0

    def loadFromJson(self, jsonData):
        self.code = jsonData["code"]
        self.airQualityIndex = jsonData["airQualityIndex"]

    def __repr__(self):
        return str(f"The code is {self.code}, \n The air quality is {self.airQualityIndex}")


class Site:
    def __init__(self):
        self.name = ""
        self.latitude = 0
        self.longitude = 0
        self.species = []

    def loadFromJson(self, jsonData):

        self.name = jsonData["name"]
        self.latitude = jsonData["latitude"]
        self.longitude = jsonData["longitude"]
        del self.species[:]
        for jsonSite in jsonData["species"]:
            species = Species()
            species.loadFromJson(jsonSite)
            self.species += [species]

    def average_air_quality(self):
        print(self.species)


def __repr__(self):
    return str(f"The name is {self.name}, \n The latitude is {self.latitude} \n  The longitude is {self.longitude}. \n The Species are {str(self.species)}")


class LocalAuthority:
    def __init__(self):
        self.name = ""
        self.sites = []

    def loadFromJson(self, jsonData):
        self.name = jsonData["name"]
        del self.sites[:]
        for jsonSite in jsonData["sites"]:
            site = Site()
            site.loadFromJson(jsonSite)
            self.sites += [site]

    def __repr__(self):
        return f"The name is {self.name}, \n The site list is {str(self.sites)}"


if __name__ == "__main__":
    js_data = read_json("./AirQuality.json")

    for data in js_data:
        authority = LocalAuthority()
        authority.loadFromJson(data)
        print(authority.sites["name"])
