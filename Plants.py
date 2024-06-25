from collections import Counter


class Field:
    def __init__(self, name):
        self.name = name
        self.__plants = []
        self.__profit = 0
        self.__plants_counter = Counter()

    def plant(self, plant_inst):
        self.__plants_counter[plant_inst] += 1
        print(self.__plants_counter)
        if self.__plants_counter[plant_inst] == 1:
            self.__plants.append(plant_inst)
        self.__profit -= plant_inst.price

    def harvest(self, plant_inst):
        if self.__plants_counter[plant_inst] > 0:
            self.__plants_counter[plant_inst] -= 1
            if self.__plants_counter[plant_inst] == 0:
                self.__plants.remove(plant_inst)
            self.__profit += plant_inst.price
            return True
        else:
            return False

    def get_current_plants(self, plant_type=None):
        print("Current plants in the field:")
        for i, plant in enumerate(self.__plants):
            if plant_type is None or plant_type == plant.__class__:
                print('Index:', i + 1)
                print(plant.get_description())
                print('Number of plants:', self.__plants_counter[plant])
                print('--------------------------------------')

        print(f"Current number of plant types: {len(self.__plants)}")

    def get_profit(self):
        return self.__profit

    def get_plants_counter(self):
        return self.__plants_counter

class Plant:
    def __init__(self, species: str, color: str, price: float, size: float):
        self.species = species
        self.color = color
        self.price = price
        self.size = size


    def get_description(self):
        raise NotImplementedError("Child classes should implement this!")

    def growth_conditions(self):
        raise NotImplementedError("Child classes should implement this!")

    def harvest_instructions(self):
        raise NotImplementedError("Child classes should implement this!")

    def use_case(self):
        raise NotImplementedError("Child classes should implement this!")