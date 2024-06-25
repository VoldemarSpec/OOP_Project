import unittest
from collections import Counter
from Plants import Field, Flower, Tree, Vegetable

class TestField(unittest.TestCase):

    def setUp(self):
        self.field = Field("Test Field")
        self.rose = Flower("Rose", "Red", 10.0, 0.5, "Spring")
        self.apple_tree = Tree("Apple Tree", "Green", 50.0, 3.0, True)
        self.carrot = Vegetable("Carrot", "Orange", 2.0, 0.2, True)

    def test_initial_field(self):
        self.assertEqual(self.field.name, "Test Field")
        self.assertEqual(self.field.get_profit(), 0)
        self.assertEqual(len(self.field.get_plants_counter()), 0)

    def test_plant(self):
        self.field.plant(self.rose)
        self.assertEqual(self.field.get_profit(), -10.0)
        self.assertEqual(self.field.get_plants_counter()[self.rose], 1)

        self.field.plant(self.apple_tree)
        self.assertEqual(self.field.get_profit(), -60.0)
        self.assertEqual(self.field.get_plants_counter()[self.apple_tree], 1)

    def test_harvest(self):
        self.field.plant(self.rose)
        self.field.plant(self.apple_tree)

        self.field.harvest(self.rose)
        self.assertEqual(self.field.get_profit(), -50.0)
        self.assertEqual(self.field.get_plants_counter()[self.rose], 0)
        self.assertNotIn(self.rose, self.field._Field__plants)

        self.field.harvest(self.apple_tree)
        self.assertEqual(self.field.get_profit(), 0.0)
        self.assertEqual(self.field.get_plants_counter()[self.apple_tree], 0)
        self.assertNotIn(self.apple_tree, self.field._Field__plants)