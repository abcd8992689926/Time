import sys

from models.config.message_api_config import MessageAPIConfig


sys.path.append(r'..\..\Libraries\python_common')
sys.path.append(r'..\..\gRPC_Server')

from file.json import Json
from log.models.config import LogConfig
logConfig = Json.load_config_as_model("config/log_config.json", LogConfig)

if __name__ == '__main__':
    test = Json.load_config_as_model("config/message_api_config.json", MessageAPIConfig)
    print(test)
from src.generated import (
    information_service_pb2_grpc,
    information_service_pb2,
    reserve_pb2
)