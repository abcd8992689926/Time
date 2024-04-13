import json
from os import abort
from typing import List

import linebot.v3.messaging
from fluent import sender
from fluent.sender import FluentSender
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import TextMessage, Message
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
        handler = WebhookHandler(mod_config.ChannelSecret)
        self._handler = handler

        @handler.add(MessageEvent, message=TextMessageContent)
        def handle_message(event):
            print(event.reply_token)
            with ApiClient(self._configuration) as api_client:
                api_instance = MessagingApi(api_client)
                api_instance.reply_message_with_http_info(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[TextMessage(text=event.message.text)]
                    )
                )

    def push_text_message(self, to: str, messages: List[Message]):
        with ApiClient(self._configuration) as api_client:
            api_instance = MessagingApi(api_client)
            messages_request = linebot.v3.messaging.PushMessageRequest(
                to=to,
                messages=messages
            )
            self._runtimeLogger.emit("Line.MessageAPI.push_text_message third_party_request",
                                     messages_request.to_dict())
            try:
                response = api_instance.push_message(messages_request)
                self._runtimeLogger.emit("Line.MessageAPI.push_text_message third_party_response",
                                         response.to_dict())
            except Exception as e:
                self._runtimeLogger.emit("Line.MessageAPI Exception", e)

    def callback(self, signature: str, body) -> bool:
        try:
            self._handler.handle(body, signature)
        except InvalidSignatureError:
            self._runtimeLogger.emit("Line.MessageAPI Exception", {
                "message": "Invalid signature. Please check your channel access token/channel secret."})
            return False

        return True
