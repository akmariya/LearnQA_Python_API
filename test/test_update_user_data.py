from lib.base_case import BaseCase
from lib.my_request import MyRequest
from lib.assertions import Assertions
from lib.user_data import user_creation_data
from lib.utils import random_str


class TestUserDataUpdate(BaseCase):

    def test_update_data_by_unauthorize_user(self):

        data = {"username": "randName"}

        response = MyRequest.put("/user/20", data=data,
                                 headers={"x-csrf-token": ""},
                                 cookies={"auth_sid": ""}
                                 )

        Assertions.assert_status_code(response, 400)
        Assertions.assert_output_text(response, "Auth token not supplied")

    def test_update_data_by_wrong_user(self):
        #регистрация пользователя
        email = random_str(5) + '@example.com'
        data = user_creation_data()
        data["email"] = email
        response = MyRequest.post("/user", data=data)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_value_has_name(response, "id")
        id = int(self.get_json_value(response, "id"))

        #login
        response2 = MyRequest.post("/user/login", data=data)
        auth_sid = self.get_cookie(response2,"auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response2, "user_id")
        assert user_id_from_auth_method == id

        #chenge data of another user
        some_id = id - 10
        data2 = {"username": "randName"}
        response3 = MyRequest.put(f"/user/{some_id}", data=data2,
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        Assertions.assert_status_code(response3, 400)
        Assertions.assert_output_text(response3, "Auth token not supplied")

    def test_change_data_with_wrong_email(self):
        # регистрация пользователя
        email = random_str(5) + '@example.com'
        data = user_creation_data()
        data["email"] = email
        response = MyRequest.post("/user", data=data)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_value_has_name(response, "id")
        id = int(self.get_json_value(response, "id"))

        # login
        response2 = MyRequest.post("/user/login", data=data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response2, "user_id")
        assert user_id_from_auth_method == id

        # change email
        data2 = {"email": "wrongemail.com"}
        response3 = MyRequest.put(f"/user/{id}", data=data2,
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )
        Assertions.assert_status_code(response3, 400)
        Assertions.assert_output_text(response3, "Invalid email format")

    def test_change_data_on_short_firstname(self):
        # регистрация пользователя
        email = random_str(5) + '@example.com'
        data = user_creation_data()
        data["email"] = email
        response = MyRequest.post("/user", data=data)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_value_has_name(response, "id")
        id = int(self.get_json_value(response, "id"))

        # login
        response2 = MyRequest.post("/user/login", data=data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response2, "user_id")
        assert user_id_from_auth_method == id

        # change firstName
        data2 = {"firstName": "m"}
        response3 = MyRequest.put(f"/user/{id}", data=data2,
                                  headers={"x-csrf-token": token},
                                  cookies={"auth_sid": auth_sid}
                                  )
        Assertions.assert_status_code(response3, 400)
        Assertions.assert_json_value_by_name(response3, "error", "Too short value for field firstName", "Wrong error")
