import click
import math


def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


class Fuel:
    def __init__(self):
        self.required_volume = 0
        self.total_volume = 0

    def add(self, volume=0):
        self.required_volume += volume
        self.total_volume += volume
        self._computed_volume(offset=volume)

    def _computed_volume(self, offset=0):
        result = int(round_down(offset / 3,  0) - 2)
        if result > 0:
            self.total_volume = self.total_volume + result
            self._computed_volume(result)


class Spaceship:
    def __init__(self, fuel=Fuel()):
        self.modules = []
        self.fuel_modules_requirements = 0
        self.fuel_requirements = 0

    def add_module(self, module):
        self.modules.append(module)
        self.fuel_modules_requirements = self.fuel_modules_requirements + module.fuel.required_volume
        self.fuel_requirements = self.fuel_requirements + module.fuel.total_volume

    def __str__(self):
        return """Spaceship:
    modules count              : %d
    fuel modules requirements  : %d
    fuel requirements : %d
        """ % (len(self.modules), self.fuel_modules_requirements, self.fuel_requirements)


class SpaceshipModule:
    def __init__(self, name="Module", weight=0):
        self.name = name
        self.weight = weight
        self.fuel = Fuel()

        self.fuel.add(volume=int(round_down(self.weight / 3,  0) - 2))

    def __str__(self):
        return """Spaceship Module:
    weight : %d
    fuel required volume : %d
    fuel total volume : %d
        """ % (self.weight, self.fuel.required_volume, self.fuel.total_volume)
