from dataclasses import dataclass


@dataclass
class TextMessage:
    type: str
    text: str
