import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
redirect_amount = len(response.history)

print("Количество редиректов: ", redirect_amount)
print("Последний URL: ", response.url)
