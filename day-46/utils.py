import datetime

def is_bad_date(date: str) -> bool:
    dates = date.split("-")
    if len(dates) == 3:
        y, m, d = dates
    else:
        return True
    good_year = y.isdigit() and int(y) <= datetime.datetime.now().year
    good_month = m.isdigit() and 1 <= int(m) <= 12
    good_day = False
    if d.isdigit() and good_month:
        if int(m) in [9,4,6,11] and 1 <= int(d) <= 30:
            good_day = True
        elif good_year and int(m) == 2:
            is_leap_year = int(y) % 4 == 0
            if is_leap_year and 1 <= int(d) <= 29:
                good_day = True
            elif not is_leap_year and 1 <= int(d) <= 28:
                good_day = True
        else:
            good_day = (1 <= int(d) <= 31)
    return not good_year or not good_month or not good_day