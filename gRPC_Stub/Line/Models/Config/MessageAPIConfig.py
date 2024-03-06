from dataclasses import dataclass
from Python_Libraries import File

@dataclass(slots=True, kw_only=True)
class MessageAPIConfig:
    ServerURL: str
    Push: str
    Multicast: str
    ChannelAccessToken: str

def test():
    PythonLibraries.Json