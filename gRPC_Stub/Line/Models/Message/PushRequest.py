from dataclasses import dataclass

from Models.Message.BaseRequest import BaseRequest


@dataclass
class PushRequest(BaseRequest):
    to: str
