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
        return len(self.__plants_counter)

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

class Flower(Plant):
    def __init__(self, species: str, color: str, price: float, size: float, blooming_season: str):
        super().__init__(species, color, price, size)
        self.blooming_season = blooming_season

    def get_description(self):
        return f"A {self.size}m {self.color} {self.species}, blooms in {self.blooming_season}. Price: {self.price}."

    def growth_conditions(self):
        return "Needs well-drained soil and full sunlight."

    def harvest_instructions(self):
        return "Cut the stem at an angle and place in water immediately."

    def use_case(self):
        return "Ideal for decorative purposes."


class Tree(Plant):
    def __init__(self, species: str, color: str, price: float, size: float, is_fruit_bearing: bool):
        super().__init__(species, color, price, size)
        self.is_fruit_bearing = is_fruit_bearing

    def get_description(self):
        desc = f"A {self.size}m {self.color} {self.species}, "
        desc += "bears fruit." if self.is_fruit_bearing else "does not bear fruit."
        return desc + f" Price: {self.price}."

    def growth_conditions(self):
        return "Needs rich, moist soil and plenty of space."

    def harvest_instructions(self):
        if self.is_fruit_bearing:
            return "Pick the fruits when ripe."
        else:
            return "No harvest instructions as it does not bear fruit."

    def use_case(self):
        return "Provides shade and can improve air quality."

class Vegetable(Plant):
    def __init__(self, species: str, color: str, price: float, size: float, is_annual: bool):
        super().__init__(species, color, price, size)
        self.is_annual = is_annual

    def get_description(self):
        desc = f"A {self.size}m {self.color} {self.species}, "
        desc += "annual plant." if self.is_annual else "perennial plant."
        return desc + f" Price: {self.price}."

    def growth_conditions(self):
        return "Requires fertile soil and regular watering."

    def harvest_instructions(self):
        return "Harvest when the vegetable reaches desired size and color."

    def use_case(self):
        return "Suitable for consumption and culinary purposes."


field = Field("My Field")
rose = Flower("Rose", "Red", 10.0, 0.5, "Spring")
apple_tree = Tree("Apple Tree", "Green", 50.0, 3.0, True)
carrot = Vegetable("Carrot", "Orange", 2.0, 0.2, True)

field.plant(rose)
field.plant(apple_tree)
field.plant(carrot)
field.harvest(rose)
print(field.get_current_plants())
print(rose.growth_conditions())
print("Current profit:", field.get_profit())
print("Current plants counter:", field.get_plants_counter())
