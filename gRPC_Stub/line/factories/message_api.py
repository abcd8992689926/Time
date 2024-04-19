import json
import sys
from os import abort
from typing import List

import grpc
import linebot.v3.messaging
import switch
from fluent import sender
from fluent.sender import FluentSender
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, TextMessageContent, Event
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    PushMessageRequest,
    Message
)
from models.config.message_api_config import MessageAPIConfig

sys.path.append(r'..\..\gRPC_Server')
from src.generated import (
    information_service_pb2_grpc,
    information_service_pb2,
    reserve_pb2
)


class MessageAPI:
    def __init__(self, mod_config: MessageAPIConfig, runtimeLogger: FluentSender):
        self._str_push_url = mod_config.ServerURL + mod_config.Push
        self._str_multicast_url = mod_config.ServerURL + mod_config.Multicast
        self._obj_header = {"Authorization": "Bearer " + mod_config.ChannelAccessToken}
        self._configuration = Configuration(
            access_token=mod_config.ChannelAccessToken
        )
        self._runtimeLogger = runtimeLogger
        self._handler = WebhookHandler(mod_config.ChannelSecret)

        @self._handler.add(MessageEvent, message=TextMessageContent)
        def handle_message(event):
            if event.message.text.startswith("/登記提醒"):
                mod_result = self.reserve(event)
                print(event)
                self.reply_message(ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text=event.message.text)]
                ))

    def push_text_message(self, mod_request: PushMessageRequest):
        with ApiClient(self._configuration) as api_client:
            api_instance = MessagingApi(api_client)
            self._runtimeLogger.emit("Line.MessageAPI.push_text_message third_party_request",
                                     mod_request.to_dict())
            try:
                response = api_instance.push_message(mod_request)
                self._runtimeLogger.emit("Line.MessageAPI.push_text_message third_party_response",
                                         response.to_dict())
            except Exception as e:
                self._runtimeLogger.emit("Line.MessageAPI.push_text_message Exception", e)

    def reply_message(self, mod_request: ReplyMessageRequest):
        with ApiClient(self._configuration) as api_client:
            api_instance = MessagingApi(api_client)
            self._runtimeLogger.emit("Line.MessageAPI.reply_message third_party_request",
                                     mod_request.to_dict())
            try:
                api_instance.reply_message_with_http_info(mod_request)

            except Exception as e:
                self._runtimeLogger.emit("Line.MessageAPI.reply_message Exception", e)

    def callback(self, signature: str, body) -> bool:
        try:
            self._handler.handle(body, signature)
        except InvalidSignatureError:
            self._runtimeLogger.emit("Line.MessageAPI Exception", {
                "message": "Invalid signature. Please check your channel access token/channel secret."})
            return False

        return True

    def reserve(self, event):
        arr_content = event.message.text.split(maxsplit=6)
        channel = grpc.insecure_channel('localhost:50053')
        stub = information_service_pb2_grpc.InformationServiceStub(channel)
        test = reserve_pb2.ReserveRequest(
            user_id=event.source.user_id,
            title=arr_content[1],
            content=arr_content[4],
            datetime=arr_content[2] + " " + arr_content[3]
        )
        print(test)
        response = stub.Reserve(test)
        return response
