import sys

from flask import Flask, request, abort
from fluent import sender

from factories.message_api import MessageAPI

if __name__ == '__main__':
    sys.path.append(r'..\..\Libraries\python_common')
    sys.path.append(r'..\..\gRPC_Server')

from file.json import Json
from models.config.message_api_config import MessageAPIConfig
from __init__ import logConfig

app = Flask(__name__)
systemLogger = sender.FluentSender('system', host=logConfig.host, port=logConfig.port)
runtimeLogger = sender.FluentSender('runtime', host=logConfig.host, port=logConfig.port)


@app.route("/callback", methods=['POST'])
def callback():
    mod_config = Json.load_config_as_model("./config/message_api_config.json", MessageAPIConfig)
    runtimeLogger.emit('LineService.PushMessage', {'message': 'get request from line service...'})
    print(request.get_data(as_text=True))
    bool_callback_result = MessageAPI(mod_config, runtimeLogger).callback(
        signature=request.headers['X-Line-Signature'],
        body=request.get_data(as_text=True)
    )
    if not bool_callback_result:
        abort(400)
    else:
        return 'OK'


if __name__ == "__main__":
    app.run(port=5000)
