import unittest
import pandas as pd
import numpy as np

from robotpt_common_utils import pandas_lib


class TestPandasLib(unittest.TestCase):

    def test_remove_consecutive_nans_from_full_list(self):
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

    def test_remove_consecutive_nans_from_one_missing(self):
        values_in = [1, np.nan, 3, 4, 5]
        values_out1 = [1, 3, 4, 5]
        values_out2 = values_in

        df_in = pd.DataFrame({
            "Values":
                values_in})
        df_out1 = pandas_lib.remove_consecutive_nans(df_in, 'Values', 0)
        test_out1 = list(df_out1.Values)
        for i in range(len(values_out1)):
            self.assertEqual(
                values_out1[i],
                test_out1[i]
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

    def test_remove_consecutive_nans_with_multiple_missing(self):

        values_in = [1, np.nan,
                     3, np.nan, np.nan,
                     4, np.nan, np.nan, np.nan,
                     5, np.nan, ]
        values_out = [1, np.nan,
                      3, np.nan, np.nan,
                      4,
                      5, np.nan, ]
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
