import unittest

from robotpt_common_utils import lists


class TestLists(unittest.TestCase):

    def test_is_iterable(self):
        self.assertFalse(lists.is_iterable(1))
        self.assertFalse(lists.is_iterable(None))
        self.assertFalse(lists.is_iterable('a'))
        self.assertFalse(lists.is_iterable('abcde'))

        self.assertTrue(lists.is_iterable('a', is_strings_iterable=True))
        self.assertTrue(lists.is_iterable('abcde', is_strings_iterable=True))

        self.assertTrue(lists.is_iterable([]))
        self.assertTrue(lists.is_iterable([1]))
        self.assertTrue(lists.is_iterable([1, 3]))
        self.assertTrue(lists.is_iterable(()))
        self.assertTrue(lists.is_iterable((1,)))
        self.assertTrue(lists.is_iterable((1, 2, 3)))

    def test_make_sure_is_iterable(self):

        self.assertEqual(
            [None],
            lists.make_sure_is_iterable(None)
        )
        self.assertEqual(
            [1],
            lists.make_sure_is_iterable(1)
        )
        self.assertEqual(
            ['obj'],
            lists.make_sure_is_iterable('obj')
        )

        self.assertEqual(
            [],
            lists.make_sure_is_iterable([])
        )
        self.assertEqual(
            [1, 2, 3],
            lists.make_sure_is_iterable([1, 2, 3])
        )
        self.assertEqual(
            (1, 2, 3),
            lists.make_sure_is_iterable((1, 2, 3))
        )

    def test_append_to_list(self):
        self.assertEqual(
            [1, 2, 3],
            lists.append_to_list([1, 2, 3], [])
        )
        self.assertEqual(
            [1, 2, 3, 4],
            lists.append_to_list([1, 2, 3], 4)
        )
        self.assertEqual(
            [1, 2, 3, 4, 5, 6],
            lists.append_to_list([1, 2, 3], [4, 5, 6])
        )
        self.assertEqual(
            [1, 2, 3, 4, 5, 6],
            lists.append_to_list(
                [1, 2, 3],
                [4, 5, 6],
                lambda x: True
            )
        )
        self.assertEqual(
            [1, 2, 3, 4, 5, 6],
            lists.append_to_list(
                [1, 2, 3],
                [4, 5, 6],
                lambda x: type(x) is int
            )
        )
        self.assertEqual(
            [1, 2, 3, 4],
            lists.append_to_list(
                [1, 2, 3],
                4,
                lambda x: type(x) is int
            )
        )
        self.assertEqual(
            [1, 2, 3, 4, 5, 6],
            lists.append_to_list(
                [1, 2, 3],
                [4, 5, 6],
                [
                    lambda x: type(x) is int,
                    lambda x: True,
                ]
            )
        )
        self.assertRaises(
            ValueError,
            lists.append_to_list,
            [1, 2, 3],
            [4, 5, 6],
            lambda x: x < 5
        )
        self.assertRaises(
            ValueError,
            lists.append_to_list,
            [1, 2, 3],
            [4, 5, 6],
            [
                lambda x: True,
                lambda x: True,
                lambda x: True,
                lambda x: True,
                lambda x: False,
            ]
        )

    def test_append_type_to_list(self):
        self.assertEqual(
            [1, 2, 3, 4],
            lists.append_type_to_list(
                [1, 2, 3],
                4,
                int
            )
        )
        self.assertEqual(
            [1, 2, 3, 4, 5],
            lists.append_type_to_list(
                [1, 2, 3],
                [4, 5],
                int
            )
        )
        self.assertEqual(
            ['ab', 'cd', 'ef', 'gh'],
            lists.append_type_to_list(
                ['ab', 'cd', 'ef'],
                'gh',
                str
            )
        )
        self.assertEqual(
            ['ab', 'cd', 'ef', 'gh', 'ij'],
            lists.append_type_to_list(
                ['ab', 'cd', 'ef'],
                ['gh', 'ij'],
                str
            )
        )
        self.assertRaises(
            ValueError,
            lists.append_type_to_list,
            [1, 2, 3],
            'foo',
            int
        )
        self.assertRaises(
            ValueError,
            lists.append_type_to_list,
            [1, 2, 3],
            [4, 'foo'],
            int
        )

    def test_is_all_elements_pass_tests(self):
        self.assertTrue(
            lists.is_all_list_elements_pass_tests(
                [1, 2, 3],
                lambda x: type(x) is int
            )
        )
        self.assertTrue(
            lists.is_all_list_elements_pass_tests(
                [1, 2, 3],
                lambda x: type(x) is int,
                lambda x: x > 0),
        )

        self.assertFalse(
            lists.is_all_list_elements_pass_tests(
                ['1', 2, 3],
                lambda x: type(x) is int,
            )
        )
        self.assertFalse(
            lists.is_all_list_elements_pass_tests(
                [0, 1, 2, 3],
                lambda x: type(x) is int,
                lambda x: x > 0
            )
        )
