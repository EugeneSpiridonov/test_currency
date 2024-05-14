from django.db import models


class Currency(models.Model):
    char_code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.char_code})"


class CurrencyRate(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        unique_together = ("currency", "date")

    def __str__(self):
        return f"{self.currency} - {self.value} on {self.date}"
