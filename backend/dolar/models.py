from django.db import models


class Dolar(models.Model):
    date = models.DateField(max_length=10, primary_key=True)
    val = models.DecimalField(max_digits=7, decimal_places=2)
    delta = models.DecimalField(max_digits=7, decimal_places=2,
                                null=True, blank=True)