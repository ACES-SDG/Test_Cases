from dateutil.parser import parse   

def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        # print('True')
        return True

    except ValueError:
        print(ValueError)
        return False

is_date("1990-12-1")

is_date("2005/3")

is_date("Jan 19, 1990")

is_date("today is 2019-03-27")

is_date("today is 2019-03-27", fuzzy=True)

is_date("Monday at 12:01am")

is_date("xyz_not_a_date")

is_date("yesterday")
