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
from linebot.v3.messaging import TextMessage, Message, PushMessageRequest
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from models.config.message_api_config import MessageAPIConfig



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
        self._dictCallbackFunction = {
            "登記提醒": self.reserve
        }

        @self._handler.add(MessageEvent, message=TextMessageContent)
        def handle_message(event):
            keywords = event.message.text.split('$')
            switch
            if len(keywords) < 2:
                return
            print(self._dictCallbackFunction.get(keywords[1]))
            mod_result = self._dictCallbackFunction.get(keywords[1])()
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
        channel = grpc.insecure_channel('localhost:50053')
        stub = information_service_pb2_grpc.InformationServiceStub(channel)
        response = stub.Reserve(
            reserve_pb2.ReserveRequest(
                user_id='test457',
                title='test title',
                content='test content'
            )
        )
