import pandas as pd


def remove_consecutive_nans(
        dataframe,
        column_name,
        max_consecutive_nans_before_remove=2
):
    if type(dataframe) is not pd.DataFrame:
        raise TypeError("'dataframe' should be a Pandas Dataframe")
    if max_consecutive_nans_before_remove < 0:
        raise ValueError("'max_consecutive_nans' should be greater than 0")

    _dataframe = dataframe.copy()
    _dataframe['Group'] = _dataframe[column_name].notnull().astype(int).cumsum()
    _dataframe = _dataframe[_dataframe[column_name].isnull()]
    _dataframe = _dataframe[
        _dataframe.Group.isin(
            _dataframe.Group.value_counts()[
                _dataframe.Group.value_counts() > max_consecutive_nans_before_remove
                ].index
        )
    ]
    _dataframe['count'] = _dataframe.groupby('Group')['Group'].transform('size')
    _dataframe.drop_duplicates(['Group'], keep='first')

    return dataframe.drop(_dataframe.index)
