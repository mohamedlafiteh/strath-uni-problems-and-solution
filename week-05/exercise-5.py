import json


def read_json(file_name):
    with open(file_name, "r", encoding="utf-8") as fjson:
        data = json.load(fjson)
        return data


if __name__ == "__main__":
    print(read_json("./AirQuality.json"))
