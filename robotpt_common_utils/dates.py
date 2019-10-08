import datetime

NUM_DAYS_IN_A_WEEK = 7


def subtract_days(start_date, end_date):

    if (
            not (type(start_date) == type(end_date) == datetime.date)
            and not (type(start_date) == type(end_date) == datetime.datetime)
    ):
        raise TypeError("Inputs must be datetimes")

    return (end_date - start_date).days


def subtract_weeks(start_date, end_date, is_full_weeks_only=True):

    weeks_difference = subtract_days(start_date, end_date) / NUM_DAYS_IN_A_WEEK
    if is_full_weeks_only:
        return int(weeks_difference)
    else:
        return weeks_difference