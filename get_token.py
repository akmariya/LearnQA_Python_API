import requests
import json
import time

URL = "https://playground.learnqa.ru/ajax/api/longtime_job"

response_start = requests.get(URL)
response_start_json = json.loads(response_start.text)
token = response_start_json["token"]
seconds = response_start_json["seconds"]

response_status = requests.get(URL, params={"token": token})
response_status_json = json.loads(response_status.text)
status_actual = response_status_json["status"]
status_expect = "Job is NOT ready"
assert status_actual, status_expect

time.sleep(seconds)

response_status2 = requests.get(URL, params={"token": token})
response_status2_json = json.loads(response_status2.text)
status_actual2 = response_status2_json["status"]
status_expect2 = "Job is ready"
assert status_actual2 == status_expect2
try:
    result = response_status2_json["result"]
    print("Поле result присутствует и равно ", result)
except KeyError:
    print("Поле result отсутствует")