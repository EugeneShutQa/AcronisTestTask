from Framework.Utils.common_utils import CommonUtils
from Framework.Logger.logger import Logger

logger = Logger(__file__).get_log()

DEFAULT_REPEAT_COUNT = 5


class PetRequestsProvider:
    def __init__(self):
        self.pet = "pet/"
        self.find_by_status_request = "findByStatus"
        self.id = "id"
        self.petId = "petId"
        self.status = "status"
        self.name = "name"
        self.category = "category"
        self.tags = "tags"
        self.photoUrls = "photoUrls"

    def find_by_status(self, request, param):
        payload = {self.status: param}
        result = request.response(self.pet + self.find_by_status_request, payload)
        return result

    def add_pet(self, request, pet_id=None, status=None, name=None, category=None, tags=None):
        if pet_id is None:
            pet_id = CommonUtils.generate_id()
        payload = {
            self.id: pet_id,
            self.status: status,
            self.name: name+str(pet_id),
            self.category: category,
            self.tags: tags
        }
        result = request.send_post_json(self.pet, payload)
        return result

    def update_pet(self, request, pet_id=None, status=None, name=None):
        """
        Some bug at this post method, got <response_code:200>, but nothing changed
        """
        payload = {
            self.status: status,
            self.name: name,
        }
        result = request.send_post_json(self.pet + str(pet_id), payload,
                                        headers={"accept": "application/json",
                                                 "Content-Type": "application/x-www-form-urlencoded"})
        return result

    def put_update_pet(self, request, payload):
        result = request.send_put_json(self.pet, payload)
        return result

    def delete_pet(self, request, pet_id=None, repeat_count=DEFAULT_REPEAT_COUNT):
        for _ in range(repeat_count):
            request.send_delete_json(self.pet + str(pet_id))

    def find_pet_by_id(self, request, pet_id, wait_code=False, repeat_count=DEFAULT_REPEAT_COUNT):
        result = request.response(self.pet + str(pet_id))
        if wait_code:
            for _ in range(repeat_count):
                result = request.response(self.pet + str(pet_id))
                if result.status_code == wait_code:
                    break
        return result
