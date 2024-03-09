import requests
from models.config.message_api_config import MessageAPIConfig
from models.message import text_message
from models.message.push_request import PushRequest
from models.message.text_message import TextMessage


class Message:
    def __init__(self, mod_config: MessageAPIConfig):
        self._str_push_url = mod_config.ServerURL + mod_config.Push
        self._str_multicast_url = mod_config.ServerURL + mod_config.Multicast
        self._obj_header = {"Authorization": "Bearer " + mod_config.ChannelAccessToken}

    """def push(self, mod_request: PushRequest[TextMessage]):
        if not mod_request.XLineRetryKey:
            self._obj_header.update({"X-Line-Retry-Key": mod_request.XLineRetryKey})
        response = requests.post(self._str_push_url, data=mod_request, headers=self._obj_header)
        print(response.json())"""


if __name__ == "__main__":
    from file.json import Json

    _mod_config = Json.load_config_as_model("../config/message_api_config.json", MessageAPIConfig)
    test = PushRequest[text_message](to="user123", messages=TextMessage(text="test_text"))
    print(test)
    """Message(_mod_config).push(
        # PushRequest("user123", "some_retry_key", [message1, message2])
        PushRequest[text_message](to="user123", messages=TextMessage(text="test_text"))
    )"""
