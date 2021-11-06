import requests


def test_cookie():
    response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
    actual_result = response.cookies.get("HomeWork")
    expected_result = "hw_value"
    assert expected_result in actual_result, "Отдается неправильная cookie"
