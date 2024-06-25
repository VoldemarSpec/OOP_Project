import unittest
from collections import Counter
from Plants import Field, Flower, Tree, Vegetable

class TestField(unittest.TestCase):

    def setUp(self):
        self.field = Field("Test Field")
        self.rose = Flower("Rose", "Red", 10.0, 0.5, "Spring")
        self.apple_tree = Tree("Apple Tree", "Green", 50.0, 3.0, True)
        self.carrot = Vegetable("Carrot", "Orange", 2.0, 0.2, True)