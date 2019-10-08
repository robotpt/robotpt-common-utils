import unittest
import datetime

from robotpt_common_utils import dates


class TestDates(unittest.TestCase):

    def test_subtract_weeks(self):
        self.assertEqual(
            0,
            dates.subtract_weeks(
                datetime.date(2019, 1, 1),
                datetime.date(2019, 1, 1),
            )
        )
        self.assertEqual(
            0,
            dates.subtract_weeks(
                datetime.date(2019, 1, 1),
                datetime.date(2019, 1, 7),
            )
        )
        self.assertEqual(
            1,
            dates.subtract_weeks(
                datetime.date(2019, 1, 1),
                datetime.date(2019, 1, 8),
            )
        )
        self.assertEqual(
            -1,
            dates.subtract_weeks(
                datetime.date(2019, 1, 8),
                datetime.date(2019, 1, 1),
            )
        )

        self.assertEqual(
            5,
            dates.subtract_weeks(
                datetime.date(2019, 1, 1),
                datetime.date(2019, 2, 5),
            )
        )
        self.assertEqual(
            -5,
            dates.subtract_weeks(
                datetime.date(2019, 2, 5),
                datetime.date(2019, 1, 1),
            )
        )
