from threading import Lock, Thread
import queue
from dataclasses import dataclass, field
from typing import Any
import time

from lcd.lcd_i2c import Lcd

lcd = Lcd(16, 2)

class SingletonMeta(type):

    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls]


@dataclass(order=True)
class Message:
    priority: int
    text: str=field(compare=False)
    due: int = 3


class ScreenManager(metaclass=SingletonMeta):

    q = queue.PriorityQueue()
    
    value: str = None

    def process_messages(self):
        while True:
            message = self.q.get()
            lcd.print(message.text, 1, 1)
            time.sleep(message.due)
            self.q.task_done()

    def start(self) -> None:
        process1 = Thread(target=self.process_messages)
        process1.start()
        
    def print(self, message: Message):
        self.q.put(message)


manager = ScreenManager()
manager.start()