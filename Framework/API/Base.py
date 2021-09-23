import requests

from Framework.Logger.logger import Logger

logger = Logger(__file__).get_log()


class ApiProvider:
    def __init__(self, site):
        self.site = site

    def response(self, get, params=None):
        logger.info("Trying to get status code")
        req = requests.get(self.site + get, params)
        return req

    def send_post_json(self, get, data, headers=None):
        logger.info("Trying to send POST request to: " + str(self.site + get) + " With data: " + str(data))
        result = requests.post(self.site + get, json=data, headers=headers)
        logger.info("Got response: " + str(result) + "With data: " + str(result.text))
        return result

    def send_put_json(self, get, data, headers=None):
        logger.info("Trying to send PUT request to: " + str(self.site + get) + " With data: " + str(data))
        result = requests.put(self.site + get, json=data, headers=headers)
        logger.info("Got response: " + str(result) + "With data: " + str(result.text))
        return result

    def send_delete_json(self, get, data=None, headers=None):
        logger.info("Trying to send DELETE request to: " + str(self.site + get) + " With data: " + str(data))
        result = requests.delete(self.site + get, json=data, headers=headers)
        logger.info("Got response: " + str(result) + "With data: " + str(result.text))
        return result
