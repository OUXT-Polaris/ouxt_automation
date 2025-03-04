import datetime
import sched


class GroundStationHeartBeat:
    def __init__(self, topic: str, timeout: float, scheduler: sched.scheduler):
        self.topic = topic
        self.timeout = timeout
        self.is_timeout = False
        self.scheduler = scheduler
        self.check_timeout(self.scheduler)

    def receive(self):
        self.last_timestamp = datetime.datetime.now()

    def check_timeout(self, scheduler):
        if self.last_timestamp:
            now = datetime.datetime.now()
            if (now - self.last_timestamp).total_seconds() >= self.timeout:
                self.is_timeout = True
        scheduler.enter(1, 2, self.check_timeout, (scheduler,))
