import json
from os import abort
from typing import List

import linebot.v3.messaging
from fluent import sender
from fluent.sender import FluentSender
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import TextMessage, Message
from models.config.message_api_config import MessageAPIConfig
from file.json import Json


class MessageAPI:
    def __init__(self, mod_config: MessageAPIConfig, runtimeLogger: FluentSender):
        self._str_push_url = mod_config.ServerURL + mod_config.Push
        self._str_multicast_url = mod_config.ServerURL + mod_config.Multicast
        self._obj_header = {"Authorization": "Bearer " + mod_config.ChannelAccessToken}
        self._configuration = linebot.v3.messaging.Configuration(
            access_token=mod_config.ChannelAccessToken
        )
        self._runtimeLogger = runtimeLogger
        self.handler = WebhookHandler(mod_config.ChannelSecret)

    def push_text_message(self, to: str, messages: List[Message]):
        with linebot.v3.messaging.ApiClient(self._configuration) as api_client:
            api_instance = linebot.v3.messaging.MessagingApi(api_client)
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
            self.handler.handle(body, signature)
        except InvalidSignatureError:
            self._runtimeLogger.emit("Line.MessageAPI Exception", {
                "message": "Invalid signature. Please check your channel access token/channel secret."})
            return False

        return True

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #echo
    msg= event.message.text
    message = TextSendMessage(text=msg)
    line_bot_api.reply_message(event.reply_token,message)

if __name__ == "__main__":
    mod_config = Json.load_config_as_model("../config/message_api_config.json", MessageAPIConfig)
    runtimeLogger = sender.FluentSender('runtime', host="localhost", port=24224)
    message_api = MessageAPI(mod_config, runtimeLogger)
    message_api.push_text_message(
        to="U6cefe412bc8a0fd54cf1d4b3465cba30",
        messages=[TextMessage(text="testText1")]
    )
    runtimeLogger.close()
