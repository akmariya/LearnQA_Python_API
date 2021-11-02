import requests

URL = "https://playground.learnqa.ru/ajax/api/compare_query_type"

response = requests.get(URL)
print(response.status_code, response.text)
# Апи отвечает "Wrong method provided" так как мы не передали никакой метод и отдает ответ 200, так как такой вариант
# ожидаем для апи

response2 = requests.head(URL)
print(response2.status_code, response2.text)
# Апи отдает ответ 400, сервер не смог обработать запрс из-за невепрного синтаксиса

method_get = {"method": "GET"}
response3 = requests.get(URL, params=method_get)
print(response3.status_code, response3.text)
# Апи отдает успешный ответ {"success":"!"}

methods = ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS", "COPY", "LINK", "UNLINK", "PURGE", "LOCK",
           "UNLOCK", "PROPFIND", "VIEW"]

for tipe in methods:
    for method in methods:
        if tipe == "GET":
            response = requests.request(tipe, URL, params={"method": method})
        else:
            response = requests.request(tipe, URL, data={"method": method})

        if tipe == method:
            if "success" not in response.text:
                print(f"Для типа запроса {tipe} и метода {method} ответ не success")
        elif "success" in response.text:
            print(f"Для типа запроса {tipe} и метода {method} ответ success")

#Для типа запроса DELETE и метода GET ответ success
#Для типа запроса PATCH и метода PATCH ответ не success
#Для типа запроса HEAD и метода HEAD ответ не success
#Для типа запроса OPTIONS и метода OPTIONS ответ не success
#Для типа запроса COPY и метода COPY ответ не success
#Для типа запроса LINK и метода LINK ответ не success
#Для типа запроса UNLINK и метода UNLINK ответ не success
#Для типа запроса PURGE и метода PURGE ответ не success
#Для типа запроса LOCK и метода LOCK ответ не success
#Для типа запроса UNLOCK и метода UNLOCK ответ не success
#Для типа запроса PROPFIND и метода PROPFIND ответ не success
#Для типа запроса VIEW и метода VIEW ответ не success
