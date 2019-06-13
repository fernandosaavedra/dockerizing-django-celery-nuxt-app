import datetime
import requests


def add_one_day(date):
    d = date.strftime('%d-%m-%Y')
    date_obj = datetime.datetime.strptime(d, '%d-%m-%Y')
    d = date_obj + datetime.timedelta(days=1)
    d = d.strftime('%d-%m-%Y')
    return d


def get_days(from_date, to_date):
    d = []
    current_date = from_date
    if(parse_date(to_date) < parse_date(from_date)):
        print('La fecha de llegada no puede ser inferior ' + 
              'a la fecha de partida')
        return False
    while current_date != to_date:
        d.append(current_date)
        curr_date_obj = datetime.datetime.strptime(current_date, '%d-%m-%Y')
        current_date = curr_date_obj + datetime.timedelta(days=1)
        current_date = current_date.strftime('%d-%m-%Y')
    d.append(to_date)
    return d


def get_currency_val(u):
    try:
        r = requests.get(url=u)
    except Exception as err:
        print('OMG! An error has been ocurred!')
        print(err)
    else:
        return r.json()['serie']


def parse_date(date):
    d = datetime.datetime.strptime(date, '%d-%m-%Y')
    return d


def parse_values(r, i, p):
    t = {}
    try:
        val = r[0]['valor']
    except Exception as e:
        val = p
    finally:
        if i <= 1:
            pass
        else:
            delta = val-float(p)
        return val, delta
