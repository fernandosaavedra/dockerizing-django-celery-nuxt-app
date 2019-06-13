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


def get_api_values(u):
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


def format_date(date):
    d = date.replace('T', ' ').replace('Z', '')
    d = datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S.%f')
    d = d.strftime('%Y-%m-%d')
    return d


def parse_values(r, i, p):
    t = {}
    try:
        t['val'] = r['valor']
    except Exception as e:
        t['val'] = p
    finally:
        if i <= 1:
            pass
        else:
            t['delta'] = round(t['val'] - p, 2)
        return t


def export_data(data):
    with open('dolar.json', 'w') as fp:
        json.dump(data, fp)


def get_dolar_data():
    dolar_values = []
    prev_val, i = (0, 0)
    years = ['2018', '2019']
    days = get_days(INIT_DATE, END_DATE)
    for y in years:
        url = 'https://mindicador.cl/api/dolar/{}'.format(y)
        serie = get_api_values(url)['serie']
        for s in reversed(serie):
            tmp_date = format_date(s['fecha'])
            j = 0
            for d in days:
                tmp = {}
                tmp['pk'] = parse_date(d)
                tmp['fields'] = parse_values(s, i, prev_val)
                dolar_values.append(tmp)
                prev_val = tmp['fields']['val']
                j += 1
                i += 1
                if tmp['pk'] == tmp_date:
                    break
            days = days[j:]
    export_data(dolar_values)


if __name__ == "__main__":
    print('Extracting dolar currency values...')
    get_dolar_data()
    print('Dolar currency exported successfully...')
