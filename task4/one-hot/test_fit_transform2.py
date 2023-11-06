import pytest
from one_hot_encoder import fit_transform


def test_fit_transform():
    cities = ["Moscow", "New York", "Moscow", "London"]
    exp_transformed_cities = [
        ("Moscow", [0, 0, 1]),
        ("New York", [0, 1, 0]),
        ("Moscow", [0, 0, 1]),
        ("London", [1, 0, 0]),
    ]
    assert fit_transform(cities) == exp_transformed_cities


def test_single_category():
    category = ["Single"]
    exp_transformed_category = [("Single", [1])]
    assert fit_transform(category) == exp_transformed_category


def test_multiple_identical_categories():
    categories = ["Identical"] * 5
    exp_transformed_categories = [("Identical", [1])] * 5
    assert fit_transform(categories) == exp_transformed_categories


def test_empty_input():
    with pytest.raises(TypeError):
        fit_transform()
