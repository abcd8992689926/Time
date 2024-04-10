from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class MessageAPIConfig:
    ServerURL: str
    Push: str
    Multicast: str
    ChannelAccessToken: str
    ChannelSecret: str
