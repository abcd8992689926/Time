from dataclasses import dataclass
from typing import List

from models.message.base_request import BaseRequest


@dataclass(slots=True, kw_only=True)
class MulticastRequest(BaseRequest):
    to: List[str]
