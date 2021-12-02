from allure_commons.types import Severity

from lib.base_case import BaseCase
from lib.my_request import MyRequest
from lib.assertions import Assertions
from lib.user_data import user_creation_data
from lib.utils import random_str
import allure


@allure.epic("Delete user")
class TestUserDelete(BaseCase):

    @allure.description("User not allowed to delete user with id 2")
    @allure.feature("Delete user. Positive case")
    @allure.severity(Severity.MINOR)
    def test_delete_user_with_id_2(self):
        id = 2
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        # login
        response = MyRequest.post("/user/login", data=data)
        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response, "user_id")
        assert user_id_from_auth_method == id

        #delete
        response2 = MyRequest.delete(f"/user/{id}",
                                     headers={"x-csrf-token": token},
                                     cookies={"auth_sid": auth_sid}
                                     )
        Assertions.assert_status_code(response2, 400)
        Assertions.assert_output_text(response2, "Please, do not delete test users with ID 1, 2, 3, 4 or 5.")

    @allure.description("User delete user")
    @allure.feature("Delete user. Positive case")
    @allure.severity(Severity.CRITICAL)
    def test_delete_user(self):
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

        #delete user
        response3 = MyRequest.delete(f"/user/{id}",
                                     headers={"x-csrf-token": token},
                                     cookies={"auth_sid": auth_sid}
                                     )
        Assertions.assert_status_code(response3, 200)

        # check user
        response4 = MyRequest.get(f"/user/{id}",
                                     headers={"x-csrf-token": token},
                                     cookies={"auth_sid": auth_sid}
                                     )
        Assertions.assert_status_code(response4, 404)
        Assertions.assert_output_text(response4, "User not found")

    @allure.description("User can't delete another user")
    @allure.feature("Delete user. Negative case")
    @allure.severity(Severity.CRITICAL)
    def test_delete_wrong_user(self):

        # create 1 user
        email = random_str(5) + '@example.com'
        data = user_creation_data()
        data["email"] = email
        response = MyRequest.post("/user", data=data)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_value_has_name(response, "id")
        id = int(self.get_json_value(response, "id"))

        # create 2 user
        email2 = random_str(5) + '@example.com'
        data2 = user_creation_data()
        data2["email"] = email2
        response = MyRequest.post("/user", data=data2)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_value_has_name(response, "id")
        id2 = int(self.get_json_value(response, "id"))

        # login
        response2 = MyRequest.post("/user/login", data=data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response2, "user_id")
        assert user_id_from_auth_method == id

        #delete user
        response3 = MyRequest.delete(f"/user/{id2}",
                                     headers={"x-csrf-token": token},
                                     cookies={"auth_sid": auth_sid}
                                     )
        Assertions.assert_status_code(response3, 200)

        response4 = MyRequest.get(f"/user/{id2}",
                                     headers={"x-csrf-token": token},
                                     cookies={"auth_sid": auth_sid}
                                     )
        Assertions.assert_json_value_has_name(response4, "username")

