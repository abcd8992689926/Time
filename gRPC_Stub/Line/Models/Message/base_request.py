from dataclasses import dataclass
from typing import TypeVar, List, Generic, Union, Optional

from models.message import text_message

TMessageType = TypeVar('TMessageType', bound=Union[text_message])


@dataclass(slots=True)
class BaseRequest(Generic[TMessageType]):
    messages: List[TMessageType]
    XLineRetryKey: Optional[str] = None
    notificationDisabled: Optional[str] = None
    customAggregationUnits: Optional[str] = None
