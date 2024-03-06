from dataclasses import dataclass

from Models.Message.BaseRequest import BaseRequest


@dataclass(slots=True, kw_only=True)
class PushRequest(BaseRequest):
    to: str
