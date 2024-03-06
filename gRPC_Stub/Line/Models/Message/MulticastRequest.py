from dataclasses import dataclass
from typing import List

from Models.Message.BaseRequest import BaseRequest


@dataclass(slots=True, kw_only=True)
class MulticastRequest(BaseRequest):
    to: List[str]
