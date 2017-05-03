import unittest


def remove_duplicates_in_order(a_list):
    """
    Write a function remove_duplicates_in_order that receives a list
    and returns a new list with the duplicates elements removed.

    Important! The elements should be in order. Example:
    remove_duplicates_in_order([2,1,1,3,4], [2,1,3,4])

    :param a_list:
    :return: a_list with no duplicates
    """
    if len(a_list) > 0:
        no_duplicates_list = []

        for i in a_list:
            if i not in no_duplicates_list:
                no_duplicates_list.append(i)
        return no_duplicates_list

    else:
        return a_list



class RemoveDuplicatesTestCase(unittest.TestCase):
    def test_remove_duplicates_in_order(self):
        self.assertEqual(remove_duplicates_in_order([2,1,1,3,4]), [2,1,3,4])

    def test_remove_duplicates_in_order_with_empty_list(self):
        self.assertEqual(remove_duplicates_in_order([]), [])

unittest.main()