import unittest
import math

from robotpt_common_utils import math_tools


class TestMath(unittest.TestCase):

    def test_round_down(self): # wrote before realizing math.ceil

        self.assertEqual(0, math_tools.round_down(0))
        self.assertEqual(1, math_tools.round_down(1))

        self.assertEqual(0, math_tools.round_down(0.1))
        self.assertEqual(0, math_tools.round_down(0.9))
        self.assertEqual(42, math_tools.round_down(42.9))

        self.assertEqual(-1, math_tools.round_down(-0.1))
        self.assertEqual(-1, math_tools.round_down(-0.9))

    def test_bound(self):

        self.assertEqual(
            0,
            math_tools.bound(0)
        )
        self.assertEqual(
            0,
            math_tools.bound(0, lower_bound=-1)
        )
        self.assertEqual(
            1,
            math_tools.bound(0, lower_bound=1)
        )

        self.assertEqual(
            -1,
            math_tools.bound(0, upper_bound=-1)
        )
        self.assertEqual(
            0,
            math_tools.bound(0, upper_bound=1)
        )

        self.assertEqual(
            0,
            math_tools.bound(0, lower_bound=-1, upper_bound=1)
        )
        self.assertEqual(
            0.5,
            math_tools.bound(0.5, lower_bound=-1, upper_bound=1)
        )
        self.assertEqual(
            -1,
            math_tools.bound(-2, lower_bound=-1, upper_bound=1)
        )
        self.assertEqual(
            1,
            math_tools.bound(2, lower_bound=-1, upper_bound=1)
        )
        self.assertEqual(
            1,
            math_tools.bound(1, lower_bound=1, upper_bound=1)
        )

        self.assertRaises(
            ValueError,
            math_tools.bound,
            0,
            lower_bound=0,
            upper_bound=-1
        )

    def test_is_int(self):
        for i in range(-100, 100):
            self.assertTrue(math_tools.is_int(i))
        for v in ['a', 'abc', None, 9.1, math.pi, math.nan]:
            self.assertFalse(math_tools.is_int(v))
