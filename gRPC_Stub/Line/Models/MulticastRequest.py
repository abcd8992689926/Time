from dataclasses import dataclass
from typing import List

from Models.BaseRequest import BaseRequest


@dataclass
class MulticastRequest(BaseRequest):
    to: List[str]
