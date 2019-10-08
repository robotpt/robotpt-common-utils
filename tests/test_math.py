import unittest

from robotpt_common_utils import math


class TestMath(unittest.TestCase):

    def test_round_down(self):

        self.assertEqual(0, math.round_down(0))
        self.assertEqual(1, math.round_down(1))

        self.assertEqual(0, math.round_down(0.1))
        self.assertEqual(0, math.round_down(0.9))
        self.assertEqual(42, math.round_down(42.9))

        self.assertEqual(-1, math.round_down(-0.1))
        self.assertEqual(-1, math.round_down(-0.9))

    def test_bound(self):

        self.assertEqual(
            0,
            math.bound(0)
        )
        self.assertEqual(
            0,
            math.bound(0, lower_bound=-1)
        )
        self.assertEqual(
            1,
            math.bound(0, lower_bound=1)
        )

        self.assertEqual(
            -1,
            math.bound(0, upper_bound=-1)
        )
        self.assertEqual(
            0,
            math.bound(0, upper_bound=1)
        )

        self.assertEqual(
            0,
            math.bound(0, lower_bound=-1, upper_bound=1)
        )
        self.assertEqual(
            0.5,
            math.bound(0.5, lower_bound=-1, upper_bound=1)
        )
        self.assertEqual(
            -1,
            math.bound(-2, lower_bound=-1, upper_bound=1)
        )
        self.assertEqual(
            1,
            math.bound(2, lower_bound=-1, upper_bound=1)
        )
        self.assertEqual(
            1,
            math.bound(1, lower_bound=1, upper_bound=1)
        )

        self.assertRaises(
            ValueError,
            math.bound,
            0,
            lower_bound=0,
            upper_bound=-1
        )

