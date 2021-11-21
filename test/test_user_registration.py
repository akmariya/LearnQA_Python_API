from lib.base_case import BaseCase
from lib.my_request import MyRequest
from lib.assertions import Assertions
import pytest
from lib.utils import random_str
from lib.user_data import user_creation_data


class TestUserRegistration(BaseCase):

    def test_registration_with_invalid_format_email(self):

        data = user_creation_data()
        data["email"] = 'vinkotovexample.com'

        response = MyRequest.post("/user", data=data)

        Assertions.assert_status_code(response, 400)
        Assertions.assert_output_text(response, "Invalid email format")
        print(response.text)

    fields = ("password", "username", "firstName", "lastName", "email")

    @pytest.mark.parametrize("empty_value", fields)
    def test_registration_without_all_data(self, empty_value):
        data = user_creation_data()
        data[empty_value] = None
        response = MyRequest.post("/user", data=data)
        Assertions.assert_status_code(response, 400)
        Assertions.assert_output_text(response, f"The following required params are missed: {empty_value}")

    def test_create_user_with_short_name(self):
        data = user_creation_data()
        shortname = "m"
        data["username"] = shortname
        response = MyRequest.post("/user", data=data)
        Assertions.assert_status_code(response, 400)
        Assertions.assert_output_text(response, f"The value of 'username' field is too short")

    def test_create_user_with_long_name(self):
        username = random_str(250)
        email = random_str(5) + '@example.com'
        data = user_creation_data()
        data["username"] = username
        data["email"] = email
        response = MyRequest.post("/user", data=data)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_value_have_name(response, "id")
