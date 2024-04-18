import json
import sys
import time
import grpc
from datetime import datetime, timezone
from concurrent import futures
from fluent import sender

if __name__ == '__main__':
    sys.path.append(r'..\..\Libraries\python_common')
    sys.path.append(r'..\..\gRPC_Server')
from database.models.future import Future
from database.repository import Repository
from src.generated import information_service_pb2_grpc, information_service_pb2, reserve_pb2
from __init__ import logConfig

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

systemLogger = sender.FluentSender('system', host=logConfig.host, port=logConfig.port)
runtimeLogger = sender.FluentSender('runtime', host=logConfig.host, port=logConfig.port)


class InformationService(information_service_pb2_grpc.InformationServiceServicer):
    def __init__(self):
        pass

    def Reserve(self, request: reserve_pb2.ReserveRequest,
                context) -> reserve_pb2.ReserveResponse:
        runtimeLogger.emit('InformationService.Reserve', {'message': 'get request from information service...'})
        with open('config/connection.json') as f:
            config = json.load(f)
        db_url = config['connectionString']
        result = True
        try:
            mod_request = Future(
                user_id=request.user_id,
                title=request.title,
                content=request.content,
                Datetime=datetime.now(timezone.utc)
            )
            print(mod_request.as_dict())
            runtimeLogger.emit('InformationService.Reserve request', mod_request.as_dict())
            Repository(db_url).add(mod_request)
            runtimeLogger.emit('InformationService.Reserve', {'message': 'successfully insert data...'})
        except Exception as e:
            runtimeLogger.emit('InformationService.Reserve Exception', e)
            result = False

        runtimeLogger.emit('InformationService.Reserve', {'message': 'return response status...'})
        runtimeLogger.close()
        return reserve_pb2.ReserveResponse(status=result)


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    information_service_pb2_grpc.add_InformationServiceServicer_to_server(InformationService(), server)
    server.add_insecure_port('[::]:50053')
    server.start()

    systemLogger.emit('InformationService', {'message': 'start service...'})
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
    finally:
        systemLogger.close()


if __name__ == '__main__':
    run()
