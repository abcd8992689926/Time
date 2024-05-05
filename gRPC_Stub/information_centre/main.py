import json
import os
import sys
import grpc
from concurrent import futures
from fluent import sender

if __name__ == '__main__':
    sys.path.append(r'..\..\Libraries\python_common')
    sys.path.append(r'..\..\gRPC_Server')
from database.models.future import Future
from database.repository import Repository
from src.generated import information_service_pb2_grpc, information_service_pb2, reserve_pb2
from __init__ import logConfig, connection_string

systemLogger = sender.FluentSender('system', host=logConfig.host, port=logConfig.port)
runtimeLogger = sender.FluentSender('runtime', host=logConfig.host, port=logConfig.port)


class InformationService(information_service_pb2_grpc.InformationServiceServicer):
    def __init__(self):
        pass

    def Reserve(self, request: reserve_pb2.ReserveRequest,
                context) -> reserve_pb2.ReserveResponse:
        runtimeLogger.emit('InformationService.Reserve', {'message': 'get request from information service...'})
        db_url = connection_string
        result = True
        print("InformationService.Reserve request: ", request)
        try:
            mod_request = Future(
                user_id=request.user_id,
                title=request.title,
                content=request.content,
                Datetime=request.datetime
            )
            print("mod_request: ", mod_request.as_dict())
            runtimeLogger.emit('InformationService.Reserve request', mod_request.as_dict())
            print(db_url)
            Repository(db_url).add(mod_request)
            print("success")
            runtimeLogger.emit('InformationService.Reserve', {'message': 'successfully insert data...'})
        except Exception as e:
            print('InformationService.Reserve Exception', e)
            runtimeLogger.emit('InformationService.Reserve Exception', e)
            result = False

        print('InformationService.Reserve', {'message': 'return response status...'})
        runtimeLogger.emit('InformationService.Reserve', {'message': 'return response status...'})
        runtimeLogger.close()
        return reserve_pb2.ReserveResponse(status=result)


def run():
    server = grpc.server(futures.ThreadPoolExecutor())
    information_service_pb2_grpc.add_InformationServiceServicer_to_server(InformationService(), server)
    server.add_insecure_port('[::]:50053')
    print("server start...")
    server.start()

    systemLogger.emit('InformationService', {'message': 'start service...'})
    server.wait_for_termination()


if __name__ == "__main__":
    run()
