from django.contrib import admin
from .models import Currency, CurrencyRate

admin.site.register(Currency)
admin.site.register(CurrencyRate)
