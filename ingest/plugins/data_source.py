from enum import Enum
from abc import abstractmethod, ABCMeta

from datetime import datetime, timezone


class DSState(Enum):
    starting = "starting"
    running = "running"
    paused = "paused"
    terminated = "terminated"
    errored = "errored"
    disabled = "disabled"

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class DataSource(metaclass=ABCMeta):

    state = None
    name = None
    runtime_id = None
    started_at = None

    def __init__(self, runtime_id, name):
        self.runtime_id = runtime_id
        self.name = name
        self.state = DSState.starting
        self.started_at = datetime.now(timezone.utc)
        print("DataSource created")

    @abstractmethod
    def migrate():
        pass

    @abstractmethod
    def collect():
        pass

    @abstractmethod
    def clean():
        pass

    @abstractmethod
    def persist():
        pass
