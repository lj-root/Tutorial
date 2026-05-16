import unittest

from algorithms.sorting import merge_sort


class MergeSortTest(unittest.TestCase):
    def test_sorts_numbers_in_ascending_order(self):
        self.assertEqual(merge_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])

    def test_handles_duplicates_and_negative_numbers(self):
        self.assertEqual(merge_sort([3, -1, 2, 3, 0, -1]), [-1, -1, 0, 2, 3, 3])

    def test_does_not_mutate_original_list(self):
        numbers = [5, 1, 4]
        sorted_numbers = merge_sort(numbers)

        self.assertEqual(sorted_numbers, [1, 4, 5])
        self.assertEqual(numbers, [5, 1, 4])

    def test_handles_empty_and_single_item_iterables(self):
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([42]), [42])


if __name__ == "__main__":
    unittest.main()
