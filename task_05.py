from datetime import datetime, timedelta


def date_in_future(num=None):
    if num:
        if isinstance(num, int):
            return (datetime.today() + timedelta(days=num)).strftime('%d-%m-%Y %H:%M:%S')
        else:
            return datetime.today().strftime('%d-%m-%Y %H:%M:%S')
    else:
        return datetime.today().strftime('%d-%m-%Y %H:%M:%S')

