from enum import Enum


class Status(Enum):
    Stopped = 1
    Loading = 2
    Playing = 3
    ShuttingDown = 4
