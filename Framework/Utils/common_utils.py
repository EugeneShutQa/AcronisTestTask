import time
import json


class CommonUtils:
    @staticmethod
    def generate_id():
        return int(time.time())


class JsonUtils:
    @staticmethod
    def get_elem_by_name(file_path, get_element):
        """
        :return: element by name from config
        """
        with open(file_path, "rb") as config_file:
            data = json.load(config_file)
            element = data[get_element]
            return element

    @staticmethod
    def get_json_from_response(response_content):
        try:
            parsed_json = json.loads(response_content)
        except (ValueError, TypeError):
            return False
        return parsed_json
