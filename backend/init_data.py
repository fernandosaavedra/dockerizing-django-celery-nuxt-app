import datetime
import json
import requests
from requests.exceptions import HTTPError


INIT_DATE = '01-01-2018'
END_DATE = datetime.date.today().strftime('%d-%m-%Y')


def get_days(from_date, to_date):
    d = []
    current_date = from_date
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
        return r.json()


def parse_date(date):
    d = datetime.datetime.strptime(date, '%d-%m-%Y')
    d = d.strftime('%Y-%m-%d')
    return d


def parse_values(r, i, p):
    t = {}
    try:
        t['val'] = r['serie'][0]['valor']
    except Exception as e:
        t['val'] = p
    finally:
        if i <= 1:
            pass
        else:
            t['delta'] = t['val'] - p
        return t


def export_data(data):
    with open('dolar.json', 'w') as fp:
        json.dump(data, fp)


def get_dolar_data():
    days_to_request = get_days(INIT_DATE, END_DATE)
    dolar_values = []
    delta, prev_val, i = (0, 0, 0)
    for day in days_to_request:
        tmp = {}
        url = 'https://mindicador.cl/api/dolar/{}'.format(day)
        request_json = get_currency_val(url)
        tmp['model'] = 'dolar.dolar'
        tmp['pk'] = parse_date(day)
        tmp['fields'] = parse_values(request_json, i, prev_val)
        prev_val = tmp['fields']['val']
        dolar_values.append(tmp)
        i = i+1
    export_data(dolar_values)


if __name__ == "__main__":
    print('Extracting dolar currency values...')
    get_dolar_data()
    print('Dolar currency exported successfully...')
