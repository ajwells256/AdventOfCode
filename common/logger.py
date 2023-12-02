

class Logger:
    def __init__(self):
        self.log_level = 3

    def set_log_level(self, level=1):
        self.log_level = level
    
    def debug(self, *args):
        if (self.log_level < 3):
            print(*args)
    
    def vdebug(self, *args):
        if (self.log_level < 2):
            print(*args)

    def vvdebug(self, *args):
        if (self.log_level < 1):
            print(*args)

    def log(self, *args):
        print(*args)

log = Logger()
