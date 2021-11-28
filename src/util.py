import datetime


def get_date(days=1, direction='negative', date_format='%Y-%m-%d'):
    if direction == 'negative':
        today = datetime.datetime.today()
        from_day = (today - datetime.timedelta(days=days)).strftime(date_format)

        return today.strftime(date_format) if days==0 else from_day
    elif direction == 'positive' : # direction positive
        today = datetime.datetime.today()
        from_day = (today + datetime.timedelta(days=days)).strftime(date_format)

        return from_day