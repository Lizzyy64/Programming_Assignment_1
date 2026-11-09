"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        self.assertEqual(hw1.vowel_count("HeLLo AEIOU"), 7)

    def test_vowel_count_empty_string(self):
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        self.assertEqual(hw1.vowel_count(""), 0)

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        lists = [[],[1,2], [1,2,3], [4,5]]
        self.assertEqual(hw1.short_lists(lists), [[1,2], [4,5]])

    def test_short_lists_no_matching_lengths(self):
        lists = [[], [1], [1, 2, 3]]
        self.assertEqual(hw1.short_lists(lists), [])

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        lists = [[5, 2], [9, 1], [1, 3]]
        self.assertEqual(hw1.ascending_pairs(lists), [[2, 5], [1, 9], [1, 3]])

    def test_ascending_pairs_other_lengths_unchanged(self):
        lists = [[], [7], [3, 2, 1], [4, 3]]
        self.assertEqual(hw1.ascending_pairs(lists), [[], [7], [3, 2, 1], [3, 4]])

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        result = hw1.add_prices(data.Price(1, 50), data.Price(2, 25))
        self.assertEqual(result, data.Price(3, 75))

    def test_add_prices_with_cents_carry(self):
        result = hw1.add_prices(data.Price(1, 75), data.Price(2, 50))
        self.assertEqual(result, data.Price(4, 25))

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        rect = data.Rectangle(data.Point(1, 1), data.Point(4, 5))
        self.assertAlmostEqual(hw1.rectangle_area(rect), 12)

    def test_rectangle_area_negative_coordinates(self):
        rect = data.Rectangle(data.Point(-3, -2), data.Point(1, 4))
        self.assertAlmostEqual(hw1.rectangle_area(rect), 24)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        b1 = data.Book(["Alice", "Bob"], "Book One")
        b2 = data.Book(["Carol"], "Book Two")
        b3 = data.Book(["Bob"], "Book Three")
        self.assertEqual(hw1.books_by_author("Bob", [b1, b2, b3]), [b1, b3])

    def test_books_by_author_no_matches(self):
        b1 = data.Book(["Alice"], "Book One")
        b2 = data.Book(["Carol"], "Book Two")
        self.assertEqual(hw1.books_by_author("Bob", [b1, b2]), [])

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        rect = data.Rectangle(data.Point(0, 0), data.Point(2, 2))
        result = hw1.circle_bound(rect)
        self.assertAlmostEqual(result.center.x, 1)
        self.assertAlmostEqual(result.center.y, 1)
        self.assertAlmostEqual(result.radius, 2 ** 0.5)

    def test_circle_bound_non_square_rectangle(self):
        rect = data.Rectangle(data.Point(0, 0), data.Point(6, 8))
        result = hw1.circle_bound(rect)
        self.assertAlmostEqual(result.center.x, 3)
        self.assertAlmostEqual(result.center.y, 4)
        self.assertAlmostEqual(result.radius, 5)

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        emps = [
            data.Employee("Ann", 10),
            data.Employee("Ben", 20),
            data.Employee("Cy", 60),
        ]
        # average is 30.0, so Ann and Ben are below
        self.assertEqual(hw1.below_pay_average(emps), ["Ann", "Ben"])

    def test_below_pay_average_empty_list(self):
        self.assertEqual(hw1.below_pay_average([]), [])


if __name__ == '__main__':
    unittest.main()
