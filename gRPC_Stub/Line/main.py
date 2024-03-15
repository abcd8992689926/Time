from typing import List

from linebot.v3.messaging import TextMessage
from output import python_pb2_grpc, python_pb2

from factories.message_api import MessageAPI


class TestService(python_pb2_grpc.GrpcServiceServicer):
    def __init__(self):
        pass

    def LinePushMessage(self, request: python_pb2.LinePushMessageRequest):
        MessageAPI().push_text_message(
            to=request.to,
            messages=[TextMessage(text=item) for item in request.text]
        )
        result = request.data + request.skill.name + " this is gprc test service"
        list_result = {"12": 1232}
        return python_pb2.LinePushMessageResponse()


def run():
    '''
    模擬服務啟動
    :return:
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GrpcServiceServicer_to_server(TestService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("start service...")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run()
