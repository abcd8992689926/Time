import grpc

from src.generated import line_service_pb2_grpc, line_service_pb2, push_message_pb2, information_service_pb2_grpc, \
    information_service_pb2, reserve_pb2


def LinePushMessageTest():
    channel = grpc.insecure_channel('localhost:50052')
    stub = line_service_pb2_grpc.LineServiceStub(channel)
    response = stub.PushMessage(
        push_message_pb2.PushMessageRequest(
            to='U6cefe412bc8a0fd54cf1d4b3465cba30',
            text=['Hello World!']
        )
    )
    print("Response received: " + str(response.status))


def InformationCentreReserveTest():
    channel = grpc.insecure_channel('localhost:50053')
    stub = information_service_pb2_grpc.InformationServiceStub(channel)
    response = stub.Reserve(
        reserve_pb2.ReserveRequest(
            user_id='test457',
            title='test title',
            content='test content'
        )
    )
    print("Response received: " + str(response.status))


if __name__ == '__main__':
    # LinePushMessageTest()
    InformationCentreReserveTest()
