import math


class three_vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def azimuthal_angle(self):
        if self.x and self.y == 0:
            return 0
        else:
            return math.atan2(self.y, self.x)

    def elevation_angle(self):
        if self.x and self.y and self.z == 0:
            return 0
        else:
            return math.atan2(math.sqrt(self.z, (self.x ** 2) + (self.y ** 2)))

    def resultant(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))


test1 = three_vector(10, 20, 30)
# print(test1.azimuthal_angle())
# print(test1.elevation_angle())
print(test1.resultant())
