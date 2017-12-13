import datetime
def add_gigasecond(birth_date):
    gigasecond = 1000000000
    birth_date += datetime.timedelta(seconds=gigasecond)
    return birth_date


