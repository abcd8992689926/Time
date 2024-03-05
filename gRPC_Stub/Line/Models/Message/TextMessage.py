from dataclasses import dataclass, field


@dataclass
class TextMessage:
    type: field(default="text", init=False, repr=False)
    text: str
