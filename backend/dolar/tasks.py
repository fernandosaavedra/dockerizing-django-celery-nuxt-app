from celery.schedules import crontab
from celery.task import periodic_task
from .models import Dolar
from .utils import *


@periodic_task(run_every=(crontab(minute='*/1')), name="task-update-dollar")
def update_dollar():
    curr_date = datetime.date.today()
    last_record = Dolar.objects.order_by('-date')[0]
    if last_record.date == curr_date:
        prev_val = Dolar.objects.order_by('-date')[1].val
        curr = curr_date.strftime('%d-%m-%Y')
        url = 'https://mindicador.cl/api/dolar/{}'.format(curr)
        r = get_currency_val(url)
        last_record.val, last_record.delta = parse_values(r,2,prev_val)
        last_record.save()
    else:
        last = add_one_day(last_record.date)
        curr = curr_date.strftime('%d-%m-%Y')
        days = get_days(last, curr)
        prev_val = last_record.val
        for d in days:
            url = 'https://mindicador.cl/api/dolar/{}'.format(d)
            r = get_currency_val(url)
            date = parse_date(d)
            val, delta = parse_values(r,2,prev_val)
            d = Dolar(date=date, val=val, delta=delta).save()
            prev_val = val
