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

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class LineService(line_service_pb2_grpc.LineServiceServicer):
    def __init__(self):
        pass

    def PushMessage(self, request: push_message_pb2.PushMessageRequest,
                    context) -> push_message_pb2.PushMessageResponse:
        mod_config = Json.load_config_as_model("./config/message_api_config.json", MessageAPIConfig)
        print(request.text)
        MessageAPI(mod_config).push_text_message(
            to=request.to,
            messages=[TextMessage(text=item) for item in request.text]
        )
        return push_message_pb2.PushMessageResponse(status=True)


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    line_service_pb2_grpc.add_LineServiceServicer_to_server(LineService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()

    print("start service...")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    print(sys.path)
    from __init__ import systemLogger

    systemLogger.emit('test2', {'key1': 'value1', 'key2': 'value2'})
    # run()
    # 最後別忘了關閉
    systemLogger.close()
