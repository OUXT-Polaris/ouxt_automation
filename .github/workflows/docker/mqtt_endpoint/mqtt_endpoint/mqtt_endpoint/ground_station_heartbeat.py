import datetime
import sched


class GroundStationHeartBeat:
    def __init__(self, topic: str, timeout: float, scheduler: sched.scheduler):
        self.last_timestamp = None
        self.topic = topic
        self.timeout = timeout
        self.is_timeout = False
        self.is_emergency = False
        self.scheduler = scheduler
        self.last_message = ""
        self.autonomous_message = "AUTO"
        self.emergency_message = "EMERGENCY"
        self.check_timeout(self.scheduler)
        self.check_last_message(self.scheduler)

    def check_last_message(self, scheduler):
        if self.last_message == self.emergency_message:
            self.is_emergency = True
        if self.last_message == self.autonomous_message:
            self.is_emergency = False
        scheduler.enter(0.1, 2, self.check_timeout, (scheduler,))

    def receive(self, message):
        self.last_message = message
        self.last_timestamp = datetime.datetime.now()

    def check_timeout(self, scheduler):
        if self.last_timestamp:
            now = datetime.datetime.now()
            if (now - self.last_timestamp).total_seconds() >= self.timeout:
                print("Heartbeat from ground station timed out!!")
                self.is_timeout = True
        scheduler.enter(0.1, 2, self.check_timeout, (scheduler,))
