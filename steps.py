import requests

from Framework.Utils.common_utils import JsonUtils
from Framework.Utils.common_utils import CommonUtils
from Page_Objects.Models.pet_models import PetModel

from Framework.Logger.logger import Logger


logger = Logger(__file__).get_log()


class PetAPISteps:
    @staticmethod
    def get_available_pets(request, pet_provider, available):
        logger.info("Trying to get response")
        response = pet_provider.find_by_status(request, available)
        CustomAsserts.assert_status_codes_are_equal(status=response.status_code,
                                                    message="'Find by status' response not received, "
                                                            "response code isn't 200")
        CustomAsserts.assert_is_json(response.content)

    @staticmethod
    def create_available_pet(api_provider, pet_provider, available, dog_name):
        logger.info("Trying to create a new 'available' pet in store")
        pet_id = CommonUtils.generate_id()
        response = pet_provider.add_pet(api_provider, status=available, name=dog_name, pet_id=pet_id)
        json_response = JsonUtils.get_json_from_response(response.content)
        new_pet = pet_provider.find_pet_by_id(api_provider, pet_id, requests.codes.ok)
        pet_model = PetModel()
        CustomAsserts.assert_status_codes_are_equal(status=response.status_code,
                                                    message="Pet wasn't added to store, response code isn't 200")
        CustomAsserts.assert_is_value_equal(first_value=pet_model.resolve_json_name(json_response),
                                            second_value=dog_name + str(pet_id),
                                            message="Pet name is not equal to sent")
        # Probably it's a bug here.
        # sometimes server won't return the new 'pet' that was created before and returns '404'.
        # Extra waits does not help.
        CustomAsserts.assert_status_codes_are_equal(status=new_pet.status_code,
                                                    message="Requested pet data wasn't returned")
        return json_response, pet_id

    @staticmethod
    def update_pet_to_sold(api_provider, pet_provider, sold, dog_name, pet_id, json_response):
        logger.info("Trying to update pet in store to status 'sold'")
        json_response["status"] = sold
        response = pet_provider.put_update_pet(api_provider, payload=json_response)
        CustomAsserts.assert_is_json(response.content)
        new_pet_response = pet_provider.find_pet_by_id(api_provider, pet_id, requests.codes.ok)
        new_pet_json_response = JsonUtils.get_json_from_response(new_pet_response.content)
        CustomAsserts.assert_is_json(response.content)

        pet_model = PetModel()
        CustomAsserts.assert_is_value_equal(first_value=pet_model.resolve_json_id(json_response),
                                            second_value=pet_id,
                                            message="Pet id is not equal to sent")
        CustomAsserts.assert_is_value_equal(first_value=pet_model.resolve_json_name(json_response),
                                            second_value=dog_name + str(pet_id),
                                            message="Pet name is not equal to sent")
        assert pet_model.resolve_json_status(new_pet_json_response) == sold, "Status has not been changed"
        return json_response

    @staticmethod
    def delete_pet_from_store(api_provider, pet_provider, pet_id):
        logger.info("Trying to delete pet in store")
        # Probably it's a bug here. Content is removed only on the 3+ time
        pet_provider.delete_pet(api_provider, pet_id)
        response = pet_provider.find_pet_by_id(api_provider, pet_id, requests.codes.not_found)
        CustomAsserts.assert_status_codes_are_equal(status=response.status_code,
                                                    expected_status=requests.codes.not_found,
                                                    message="Requested pet data was returned after deletion")


class CustomAsserts:
    @staticmethod
    def assert_is_json(file):
        assert JsonUtils.get_json_from_response(file) is not False, "Response is not in JSON format"

    @staticmethod
    def assert_is_value_equal(first_value, second_value, message):
        assert first_value == second_value, message
    
    @staticmethod
    def assert_status_codes_are_equal(status, message, expected_status=requests.codes.ok):
        assert status == expected_status, message
