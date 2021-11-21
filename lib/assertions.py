from requests import Response
import json


class Assertions:

    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is't in JSON format. Response text is {response.text}"

        assert name in response_as_dict, f"Response JSON doesn't have key {name}"
        return response_as_dict[name] == expected_value, error_message

    @staticmethod
    def assert_json_value_have_name(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is't in JSON format. Response text is {response.text}"

        assert name in response_as_dict, f"Response JSON doesn't have key {name}"


    @staticmethod
    def assert_status_code(response: Response, expected_value):
        assert response.status_code == expected_value, f"Unexpected status code. Code {response.status_code} instead" \
                                                       f"of {expected_value}"

    @staticmethod
    def assert_output_text(response: Response, expected_value):
        assert response.text == expected_value, f"Wrong output. Expect {expected_value}, got {response.text}"
