import grpc

from output import python_pb2_grpc, python_pb2


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = python_pb2_grpc.GrpcServiceStub(channel)
    response = stub.LinePushMessage(
        python_pb2.LinePushMessageRequest(
            to='U6cefe412bc8a0fd54cf1d4b3465cba30',
            text='Hello World!'
        )
    )
    print("Response received: " + response.your_response_field)


if __name__ == '__main__':
    run()
