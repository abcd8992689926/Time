import grpc

from src.generated import line_service_pb2_grpc, line_service_pb2, push_message_pb2


def run():
    channel = grpc.insecure_channel('localhost:50052')
    stub = line_service_pb2_grpc.LineServiceStub(channel)
    response = stub.PushMessage(
        push_message_pb2.PushMessageRequest(
            to='U6cefe412bc8a0fd54cf1d4b3465cba30',
            text=['Hello World!']
        )
    )
    print("Response received: " + str(response.status))


if __name__ == '__main__':
    run()
