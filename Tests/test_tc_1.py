import pytest

from steps import PetAPISteps
from Framework.API.Base import ApiProvider
from Page_Objects.requests.pet_requests import PetRequestsProvider
from Framework.Utils.common_utils import JsonUtils
from Framework.Logger.logger import Logger

logger = Logger(__file__).get_log()


data_file = 'Resources/testdata.json'
test_data = JsonUtils.get_elem_by_name(data_file, "testdata")


class TestPetStore:
    @pytest.mark.parametrize("available, sold, dog_name", test_data)
    def test_create_update_and_delete_pet(self, load_config, available, sold, dog_name):
        api_provider = ApiProvider(load_config)
        pet_provider = PetRequestsProvider()

        PetAPISteps.get_available_pets(api_provider, pet_provider, available)
        json_response, pet_id = PetAPISteps.create_available_pet(api_provider, pet_provider, available, dog_name)
        PetAPISteps.update_pet_to_sold(api_provider, pet_provider, sold, dog_name, pet_id, json_response)
        PetAPISteps.delete_pet_from_store(api_provider, pet_provider, pet_id)
