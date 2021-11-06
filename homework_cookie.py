import requests


def test_cookie():
    response = requests.get("https://playground.learnqa.ru/api/homework_cookie")

    actual_cookie_name = response.headers.get("Set-cookie")
    expect_cookie_name = "HomeWork"
    assert expect_cookie_name in actual_cookie_name, "Неправильное название cookie"
    
    actual_result = response.cookies.get("HomeWork")
    expected_result = "hw_value"
    assert expected_result in actual_result, "Отдается неправильная cookie"
