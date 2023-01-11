import logging
from systemd.journal import JournalHandler


class Logger:
    def __init__(self):
        self.log = logging.getLogger('test')
        
        log_fmt = logging.Formatter("%(levelname)s %(message)s")
        log_ch = JournalHandler()
        log_ch.setFormatter(log_fmt)

        self.log.addHandler(log_ch)
        self.log.setLevel(logging.DEBUG)

    def warning(self, message):
        self.log.warning(message)

    def info(self, message):
        self.log.info(message)

    def error(self, message):
        self.log.error(message)

    def debug(self, message):
        self.log.debug(message)
