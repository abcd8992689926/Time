from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class Response:
    success: bool
    reply_message: str
