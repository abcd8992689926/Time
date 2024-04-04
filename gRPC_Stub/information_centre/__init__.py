import sys


sys.path.append('..\..\Libraries\python_common')
sys.path.append('..\..\gRPC_Server')

from file.json import Json
from log.models.config import LogConfig
logConfig = Json.load_config_as_model("config/log_config.json", LogConfig)