from dataclasses import dataclass


@dataclass(slots=True, kw_only=True)
class LogConfig:
    host: str
    port: int
