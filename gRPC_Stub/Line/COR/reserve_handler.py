import grpc
from COR import information_centre_config
from COR.base_handler import BaseHandler
from models.handler.response import Response

from src.generated import (
    information_service_pb2_grpc,
    information_service_pb2,
    reserve_pb2
)


class ReserveHandler(BaseHandler):
    def __init__(self, successor=None):
        self.information_centre_config = information_centre_config
        super().__init__(successor)

    def handle_request(self, event) -> Response:
        if event.message.text.startswith("/登記提醒"):
            mod_result = self.reserve(event)
            mod_response = Response(
                success=mod_result,
                reply_message="登記成功"
            )
            return mod_response
        else:
            super().handle_request(event)

    def reserve(self, event) -> bool:
        arr_content = event.message.text.split(maxsplit=3)
        host = self.information_centre_config["host"]
        port = self.information_centre_config["port"]
        with grpc.secure_channel(
                f"{host}:{port}", grpc.ssl_channel_credentials(),
                options=(("grpc.enable_http_proxy", 0),)
        ) as channel:
            stub = information_service_pb2_grpc.InformationServiceStub(channel)
            response = stub.Reserve(reserve_pb2.ReserveRequest(
                user_id=event.source.user_id,
                title=arr_content[1],
                content=arr_content[2],
                datetime=arr_content[3]
            )).status
            print("response:", response)
            return response
