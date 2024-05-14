# test_currency

# Задача: Собрать курсы валют со страницы https://www.cbr-xml-daily.ru/daily_json.js

- Команда `python manage.py fetch_rates` собирает курсы валют (по умолчанию - на дату 14.05.2024!) и заносит их в БД.
- Если вы хотите указать другую дату, вы можете сделать это, передав ее в качестве аргумента:
`python manage.py fetch_rates --date=2024-05-15`
