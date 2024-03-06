from dataclasses import dataclass, field


@dataclass(slots=True, kw_only=True)
class TextMessage:
    type: field(default="text", init=False, repr=False)
    text: str
