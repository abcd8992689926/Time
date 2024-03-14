import sys

from models.config.message_api_config import MessageAPIConfig

sys.path.append('..\..\Libraries\python_common')
sys.path.append('..\..\gRPC_Server\output')

from file.json import Json

if __name__ == '__main__':
    test = Json.load_config_as_model("config/message_api_config.json", MessageAPIConfig)
    print(test)
