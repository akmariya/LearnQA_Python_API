from lib.base_case import BaseCase
from lib.my_request import MyRequest
from lib.assertions import Assertions


class TestAuthorizedUser(BaseCase):

    def setup(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response1 = MyRequest.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response1,"auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

    def test_get_info_for_wrong_id(self):

        some_id = self.user_id_from_auth_method - 1

        response2 = MyRequest.get(
            f"/user/{some_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_status_code(response2, 200)
        Assertions.assert_json_value_has_name(response2, "username")
        Assertions.assert_json_value_has_not_name(response2, "email")
        Assertions.assert_json_value_has_not_name(response2, "firstName")
        Assertions.assert_json_value_has_not_name(response2, "lastName")
