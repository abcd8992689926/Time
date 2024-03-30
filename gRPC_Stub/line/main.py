import atexit
import logging
import sys
import time
from concurrent import futures
from typing import List

import grpc
from linebot.v3.messaging import TextMessage
from fluent import sender

if __name__ == '__main__':
    sys.path.append('..\..\gRPC_Server')
from src.generated import line_service_pb2_grpc, line_service_pb2, push_message_pb2
from file.json import Json
from factories.message_api import MessageAPI
from models.config.message_api_config import MessageAPIConfig
from __init__ import logConfig

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

systemLogger = sender.FluentSender('system', host=logConfig.host, port=logConfig.port)
runtimeLogger = sender.FluentSender('runtime', host=logConfig.host, port=logConfig.port)
class LineService(line_service_pb2_grpc.LineServiceServicer):
    def __init__(self):
        pass

    def PushMessage(self, request: push_message_pb2.PushMessageRequest,
                    context) -> push_message_pb2.PushMessageResponse:
        mod_config = Json.load_config_as_model("./config/message_api_config.json", MessageAPIConfig)
        runtimeLogger.emit('LineService.PushMessage', {'message': 'get request from line service...'})
        MessageAPI(mod_config, runtimeLogger).push_text_message(
            to=request.to,
            messages=[TextMessage(text=item) for item in request.text]
        )
        runtimeLogger.emit('LineService.PushMessage', {'message': 'return response status...'})
        runtimeLogger.close()
        return push_message_pb2.PushMessageResponse(status=True)


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    line_service_pb2_grpc.add_LineServiceServicer_to_server(LineService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()

    systemLogger.emit('LineService', {'message': 'start service...'})
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
    finally:
        systemLogger.close()


if __name__ == '__main__':
    run()
