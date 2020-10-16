"""
A class to represent a solar panel that is mounted 
on a building.
"""


class SolarPanel:
    def __init__(self, serialNumber, currentPower):
        self.serialNumber = serialNumber
        self.currentPower = currentPower


"""
A class to represent a set of solar panels that are
mounted on the same building.
"""


class SolarArray:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.solarPanels = []

    """
    A function to calculate the total power of the solar
    panels that are on this building.
    """

    def totalPower(self):
        total = 0.0
        for solarPanel in self.solarPanels:
            total += solarPanel.currentPower
        return total


if __name__ == "__main__":
    solarArray = SolarArray(12, 13)
    solarArray.solarPanels += [SolarPanel("XXS-213", 10)]
    solarArray.solarPanels += [SolarPanel("XYS-233", 9)]
    print(solarArray.totalPower())