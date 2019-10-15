import unittest
import pandas as pd
import numpy as np

from robotpt_common_utils import pandas_lib


class TestRemoveConsecutiveNans(unittest.TestCase):

    def test_full_list(self):
        values = [1, 2, 3, 4, 5]
        df_in = pd.DataFrame({
            "Values":
                values})
        for j in range(10):
            df_out = pandas_lib.remove_consecutive_nans(df_in, 'Values', j)
            for i in range(len(values)):
                self.assertEqual(
                    values[i],
                    df_out.Values[i]
                )

    def test_one_missing(self):
        values_in = [1, np.nan, 3, 4, 5]
        values_out1 = values_in
        values_out2 = [1, 3, 4, 5]

        df_in = pd.DataFrame({
            "Values":
                values_in})
        df_out1 = pandas_lib.remove_consecutive_nans(df_in, 'Values', 0)
        test_out1 = list(df_out1.Values)
        for i in range(len(values_out1)):
            true_val = values_out1[i]
            test_val = test_out1[i]
            if np.isnan(true_val):
                self.assertTrue(np.isnan(test_val))
            else:
                self.assertEqual(
                    true_val, test_val
                )

        df_out2 = pandas_lib.remove_consecutive_nans(df_in, 'Values', 1)
        test_out2 = list(df_out2.Values)
        for i in range(len(values_out2)):
            true_val = values_out2[i]
            test_val = test_out2[i]
            if np.isnan(true_val):
                self.assertTrue(np.isnan(test_val))
            else:
                self.assertEqual(
                    true_val, test_val
                )

    def test_multiple_missing(self):

        values_in = [1, np.nan,
                     3, np.nan, np.nan,
                     4, np.nan, np.nan, np.nan,
                     5, np.nan, ]
        values_out = [1,
                      3,
                      4, np.nan, np.nan, np.nan,
                      5, ]
        df_in = pd.DataFrame({"Values": values_in})

        df_out = pandas_lib.remove_consecutive_nans(df_in, 'Values', 2)
        test_out = list(df_out.Values)
        for i in range(len(values_out)):
            true_val = values_out[i]
            test_val = test_out[i]
            if np.isnan(true_val):
                self.assertTrue(np.isnan(test_val))
            else:
                self.assertEqual(
                    true_val, test_val
                )


class TestSplitOnMain(unittest.TestCase):

    def test_output(self):

        values_in = [0,
                     1, np.nan,
                     2, np.nan, np.nan,
                     3, np.nan, np.nan, np.nan,
                     ]
        values_out = [[0, 1],
                      [2],
                      [3]]
        df_in = pd.DataFrame({"Values": values_in})
        test_out = pandas_lib.split_on_nan(df_in, 'Values')

        for i in range(len(values_out)):
            true_val = values_out[i]
            test_val = list(test_out[i]["Values"])
            for j in range(len(true_val)):
                self.assertEqual(
                    true_val[j], test_val[j]
                )
