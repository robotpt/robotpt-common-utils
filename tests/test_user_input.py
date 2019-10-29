import unittest

from robotpt_common_utils import user_input


class TestUserInput(unittest.TestCase):

    def test_is_yes(self):

        for y in ['YES', 'YUP', 'yeAh']:
            self.assertTrue(user_input.is_yes(y))
        for n in ['No', 'Nope', 'NaH']:
            self.assertFalse(user_input.is_yes(n))
        for s in ['Bah', 'Wah', 'Dope', 'a', 'b']:
            self.assertRaises(
                ValueError,
                user_input.is_yes,
                s
            )
        for arg in [None, int, 1, 3, input]:
            self.assertRaises(
                TypeError,
                user_input.is_yes,
                arg
            )
