from dataclasses import dataclass
from typing import TypeVar, List

TMessageType = TypeVar('TMessageType')


@dataclass
class BaseRequest:
    XLineRetryKey: str
    messages: List[TMessageType]
    notificationDisabled: str
    customAggregationUnits: str
