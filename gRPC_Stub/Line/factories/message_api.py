from typing import List

import linebot.v3.messaging
from linebot.v3.messaging import TextMessage, Message
from models.config.message_api_config import MessageAPIConfig
from file.json import Json


class MessageAPI:
    def __init__(self, mod_config: MessageAPIConfig):
        self._str_push_url = mod_config.ServerURL + mod_config.Push
        self._str_multicast_url = mod_config.ServerURL + mod_config.Multicast
        self._obj_header = {"Authorization": "Bearer " + mod_config.ChannelAccessToken}
        self._configuration = linebot.v3.messaging.Configuration(
            access_token=mod_config.ChannelAccessToken
        )

    def push_text_message(self, to: str, messages: List[Message]):
        with linebot.v3.messaging.ApiClient(self._configuration) as api_client:
            api_instance = linebot.v3.messaging.MessagingApi(api_client)
            messages_request = linebot.v3.messaging.PushMessageRequest(
                to=to,
                messages=messages
            )
            print(messages_request)

            try:
                api_instance.push_message(messages_request)
                print("The response of MessagingApi->push_message:\n")
            except Exception as e:
                print("Exception when calling MessagingApi->push_message: %s\n" % e)


if __name__ == "__main__":
    mod_config = Json.load_config_as_model("../config/message_api_config.json", MessageAPIConfig)
    message_api = MessageAPI(mod_config)
    message_api.push_text_message(
        to="U6cefe412bc8a0fd54cf1d4b3465cba30",
        messages=[TextMessage(text="testText1")]
    )
