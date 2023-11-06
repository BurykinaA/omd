import unittest
from one_hot_encoder import fit_transform  # замените на имя вашего модуля


class TestFitTransform(unittest.TestCase):
    def test_fit_transform(self):
        cities = ["Moscow", "New York", "Moscow", "London"]
        exp_transformed_cities = [
            ("Moscow", [0, 0, 1]),
            ("New York", [0, 1, 0]),
            ("Moscow", [0, 0, 1]),
            ("London", [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_single_category(self):
        category = ["Single"]
        exp_transformed_category = [("Single", [1])]
        transformed_category = fit_transform(category)
        self.assertEqual(transformed_category, exp_transformed_category)

    def test_multiple_identical_categories(self):
        categories = ["Identical"] * 5
        exp_transformed_categories = [("Identical", [1])] * 5
        transformed_categories = fit_transform(categories)
        self.assertEqual(transformed_categories, exp_transformed_categories)


if __name__ == "__main__":
    unittest.main()
