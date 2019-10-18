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

    def test_get_date_range_single_increment(self):
        for range_length in range(10):
            start_date = datetime.date(2019, 10, 1)
            end_date = start_date + datetime.timedelta(days=range_length)
            truth_date_range = [
                start_date + datetime.timedelta(days=i) for i in range(range_length)
            ]
            test_date_range = dates.get_date_range(start_date, end_date)
            self.assertEqual(
                range_length,
                len(test_date_range),
            )
            for i in range(range_length):
                self.assertEqual(
                    truth_date_range[i],
                    test_date_range[i]
                )

    def test_get_date_range_multiple_increment(self):

        for increment in range(1, 10):
            range_length = 3
            start_date = datetime.date(2019, 10, 1)
            end_date = start_date + datetime.timedelta(days=range_length*increment)
            truth_date_range = [
                start_date + datetime.timedelta(days=i*increment) for i in range(range_length)
            ]
            test_date_range = dates.get_date_range(start_date, end_date, increment)
            self.assertEqual(
                range_length,
                len(test_date_range),
            )
            for i in range(len(truth_date_range)):
                self.assertEqual(
                    truth_date_range[i],
                    test_date_range[i]
                )

    def test_format_date_from_get_date_range(self):
        start_date = datetime.date(2019, 10, 1)
        end_date = start_date + datetime.timedelta(days=3)
        truth_date_range = [
            '2019-10-01',
            '2019-10-02',
            '2019-10-03',
        ]
        test_date_range = dates.get_date_range(
            start_date,
            end_date,
            output_format='%Y-%m-%d'
        )
        self.assertEqual(
            len(truth_date_range),
            len(test_date_range),
        )
        for i in range(len(truth_date_range)):
            self.assertEqual(
                truth_date_range[i],
                test_date_range[i]
            )
