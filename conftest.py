import pytest
from Framework.Utils.common_utils import JsonUtils


@pytest.fixture(scope="session")
def load_config():
    config_file = 'Resources/config.json'
    api_host = JsonUtils.get_elem_by_name(config_file, "API_HOST")
    return api_host
