class PetModel:
    def __init__(self):
        self.id = "id"
        self.name = "name"
        self.status = "status"

    def resolve_json_id(self, json):
        result = json.get(self.id)
        return result

    def resolve_json_status(self, json):
        result = json.get(self.status)
        return result

    def resolve_json_name(self, json):
        result = json.get(self.name)
        return result
