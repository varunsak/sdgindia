from django.db import models


class PortData(models.Model):
    product = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=19, decimal_places=10)
    unit = models.CharField(max_length=200)
    item_rate_inv = models.DecimalField(max_digits=19, decimal_places=10)
    currency = models.CharField(max_length=200)
    total_amount = models.DecimalField(max_digits=19, decimal_places=10)
    fob_inr = models.DecimalField(max_digits=19, decimal_places=10)
    item_rate_inr = models.DecimalField(max_digits=19, decimal_places=10)
    fob_usd = models.DecimalField(max_digits=19, decimal_places=10)
    foreign_port = models.CharField(max_length=200)
    foreign_country = models.CharField(max_length=200)
    india_port = models.CharField(max_length=200)
    india_company = models.CharField(max_length=200)
    foreign_company = models.CharField(max_length=200)
    invoice_number = models.CharField(max_length=200)
    hs_code = models.CharField(max_length=200)

