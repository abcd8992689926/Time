import sys

from fluent import sender

from models.config.message_api_config import MessageAPIConfig
from models.config.log_config import LogConfig

sys.path.append('..\..\Libraries\python_common')
sys.path.append('..\..\gRPC_Server')

from file.json import Json
logConfig = Json.load_config_as_model("config/log_config.json", LogConfig)
systemLogger = sender.FluentSender('system', host=logConfig.host, port=logConfig.port)
runtimeLogger = sender.FluentSender('runtime', host=logConfig.host, port=logConfig.port)

if __name__ == '__main__':
    test = Json.load_config_as_model("config/message_api_config.json", MessageAPIConfig)
    print(test)
