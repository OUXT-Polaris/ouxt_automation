import datetime
import sched


class GroundStationHeartBeat:
    def __init__(self, topic: str, timeout: float):
        self.last_timestamp = None
        self.topic = topic
        self.timeout = timeout
        self.is_timeout = False

    def receive(self):
        self.last_timestamp = datetime.datetime.now()
