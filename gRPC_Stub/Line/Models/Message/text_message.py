from dataclasses import dataclass, field


@dataclass(slots=True)
class TextMessage:
    type: field(default="text", init=False, repr=False)
    text: str

    def __init__(self, text: str):
        self.type = "text"
        self.text = text
