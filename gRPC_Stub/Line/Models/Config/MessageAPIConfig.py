import sys
from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class MessageAPIConfig:
    ServerURL: str
    Push: str
    Multicast: str
    ChannelAccessToken: str


if __name__ == '__main__':
    load_config_as_model