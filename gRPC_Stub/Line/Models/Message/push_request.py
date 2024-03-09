from dataclasses import dataclass
from typing import TypeVar, Union

from models.message import text_message
from models.message.base_request import BaseRequest, TMessageType


@dataclass(slots=True)
class PushRequest(BaseRequest[TMessageType]):
    to: str = ""
