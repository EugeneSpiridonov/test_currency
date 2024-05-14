from django.http import JsonResponse
from .models import CurrencyRate
from datetime import datetime


def show_rates(request):
    date_str = request.GET.get("date")
    if date_str is None:
        return JsonResponse({"error": "Missing date parameter."}, status=400)
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        rates = CurrencyRate.objects.filter(date=date)
        data = [{"currency": rate.currency.name, "value": rate.value} for rate in rates]
        return JsonResponse(data, safe=False)
    except ValueError:
        return JsonResponse(
            {"error": "Invalid date format. Please use YYYY-MM-DD."}, status=400
        )
