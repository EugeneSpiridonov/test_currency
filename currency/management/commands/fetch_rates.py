import requests
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date
from currency.models import Currency, CurrencyRate
from datetime import datetime


class Command(BaseCommand):
    help = "Fetches currency rates from the Central Bank of Russia for a given date and saves them to the database."

    def add_arguments(self, parser):
        parser.add_argument(
            "--date",
            type=str,
            help="Date in the format YYYY-MM-DD",
            default="2024-05-14",
        )

    def handle(self, *args, **kwargs):
        date_str = kwargs["date"]
        date = parse_date(date_str)

        if not date:
            self.stdout.write(self.style.ERROR("Invalid date format"))
            return

        url = f"https://www.cbr-xml-daily.ru/archive/{date.year}/{date.month:02d}/{date.day:02d}/daily_json.js"
        response = requests.get(url)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR("Failed to fetch data from the API"))
            return

        data = response.json()

        for code, details in data["Valute"].items():
            char_code = details["CharCode"]
            name = details["Name"]
            value = details["Value"]

            currency, _ = Currency.objects.get_or_create(
                char_code=char_code, defaults={"name": name}
            )

            rate, created = CurrencyRate.objects.get_or_create(
                currency=currency, date=date, defaults={"value": value}
            )

            if not created:
                rate.value = value
                rate.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully fetched and saved currency rates for {date_str}."
            )
        )
