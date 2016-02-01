__author__ = 'Gaurav Khanna'

import unittest
import proboscis.asserts
from proboscis import test

import utils

@test(groups=["unit", "numbers"])
class TestIsNegative(unittest.TestCase):
    """Confirm that utils.is_negative works correctly."""

    def test_should_return_true_for_negative_numbers(self):
        self.assertTrue(utils.is_negative(-47))

    def test_should_return_false_for_positive_numbers(self):
        self.assertFalse(utils.is_negative(56))

    def test_should_return_false_for_zero(self):
        self.assertFalse(utils.is_negative(0))