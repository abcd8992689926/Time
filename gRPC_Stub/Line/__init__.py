import sys

from models.config.message_api_config import MessageAPIConfig

sys.path.append('..\..\Libraries\python_common')

from file.json import Json

test = Json.load_config_as_model("config/message_api_config.json", MessageAPIConfig)
print(test)
