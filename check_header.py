import requests


def test_cookie():
    response = requests.get("https://playground.learnqa.ru/api/homework_header")

    actual_headers = response.headers
    expect_part_of_header = "x-secret-homework-header"
    assert expect_part_of_header in actual_headers, "Неправильное название cookie"

    actual_header = response.headers.get("x-secret-homework-header")
    expect_header = "Some secret value"
    assert expect_header in actual_header, "Неправильное название header"
