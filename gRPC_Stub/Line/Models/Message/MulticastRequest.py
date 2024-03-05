from dataclasses import dataclass
from typing import List

from Models.Message.BaseRequest import BaseRequest


@dataclass
class MulticastRequest(BaseRequest):
    to: List[str]
