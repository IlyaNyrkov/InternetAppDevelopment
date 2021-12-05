from django.db import models

# Create your models here.
class crypto_currency(models.Model):
    name = models.CharField("currency name", max_length=20)
    dollar_price = models.FloatField("price in dollars", max_length=10)
    euro_price = models.FloatField("price in euros", max_length=10)
    rubles_price = models.FloatField("price in rubles", max_length=16)
    logo = models.ImageField("logo")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'