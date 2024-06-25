import unittest
from collections import Counter
from unittest.mock import patch
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

    @patch('builtins.print')
    def test_get_current_plants(self, mock_print):
        self.field.plant(self.rose)
        self.field.plant(self.apple_tree)
        self.field.plant(self.carrot)

        self.field.get_current_plants()

        mock_print.assert_any_call("Current plants in the field:")
        mock_print.assert_any_call('Index:', 1)
        mock_print.assert_any_call('A 0.5m Red Rose, blooms in Spring. Price: 10.0.')
        mock_print.assert_any_call('Number of plants:', 1)
        mock_print.assert_any_call('--------------------------------------')
        mock_print.assert_any_call('Index:', 2)
        mock_print.assert_any_call('A 3.0m Green Apple Tree, bears fruit. Price: 50.0.')
        mock_print.assert_any_call('Number of plants:', 1)
        mock_print.assert_any_call('--------------------------------------')
        mock_print.assert_any_call('Index:', 3)
        mock_print.assert_any_call('A 0.2m Orange Carrot, annual plant. Price: 2.0.')
        mock_print.assert_any_call('Number of plants:', 1)
        mock_print.assert_any_call('--------------------------------------')
        mock_print.assert_any_call('Current number of plant types: 3')