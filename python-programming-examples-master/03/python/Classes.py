#!/usr/bin/env python3

class Computer():
    def __init__(self, cpu):
        self.address = ""
        self.cpu = cpu
        self.ram = 0
        self.__privateInfo = "secrets"

    def __str__(self):
        stringValue = "{address=\"" + self.address + "\""
        stringValue += ", cpu=" + str(self.cpu)
        stringValue += ", ram=" + str(self.ram)
        stringValue += ", privateInfo=" + str(self.__privateInfo)
        stringValue += "}"
        return stringValue

    def __repr__(self):
        return self.__str__()

class SuperComputer(Computer):
    def __init__(self, cpu):
        Computer.__init__(self, cpu * 10)
        self.ram = 100

def classes():
    pc = Computer(2)
    pc.address = "127.0.0.1"
    pc.ram = 10
    pc.__privateInfo = "hacked"
    print("pc=" + str(pc))

    superPC = SuperComputer(3)
    print("superPC=" + str(superPC))

    farm = []
    for i in range(10):
        pc = Computer(4)
        pc.ram = 4
        pc.address = "192.168.0." + str(10 + i)
        farm += [ pc ]

    print("farm=" + str(farm))

if __name__ == "__main__":
    classes()