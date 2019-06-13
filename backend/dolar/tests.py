from django.test import TestCase
from .models import Dolar
from .utils import *


class UtilsTestCase(TestCase):
    def setUp(self):
        self.date = datetime.datetime(2018, 12, 12)
        self.d_from = '10-10-2011'
        self.d_to = '13-10-2011'
        self.url_to_check = 'https://mindicador.cl/'\
                            'api/dolar/11-06-2019'
        self.date_to_parse = '12-12-2018'
        self.response = [{'fecha':'2019-06-11T04:00:00.000Z',
                          'valor':697.34}]

    def test_add_one_day(self):
        self.assertEqual(add_one_day(self.date),
                         '13-12-2018')

    def test_get_days(self):
        arr = ['10-10-2011','11-10-2011','12-10-2011',
               '13-10-2011']
        self.assertEqual(get_days(self.d_from, self.d_to), 
                         arr)

    def test_get_days_false(self):
        self.assertEqual(get_days(self.d_to, self.d_from), 
                         False)
    
    def test_get_currency_val(self):
        self.assertEqual(get_currency_val(self.url_to_check),
                         self.response)
    
    def test_parse_date(self):
        self.assertEqual(parse_date(self.date_to_parse), 
                         self.date)
    
    def test_parse_values(self):
        prev_val = 697.34
        i = 10
        returned_value = 697.34, 0
        self.assertEqual(parse_values(self.response, i, prev_val), 
                         returned_value)