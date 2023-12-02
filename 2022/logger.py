
class logger:
    def __init__(self):
        self.debug_def = False

    def setLevel(self, level):
        if level == 'debug':
            self.debug_def = True

    def debug(self, *args):
        if (self.debug_def):
            for arg in args:
                print(arg, end=" ")
            print("")
                
    def warn(self, *args):
        print("WARN ", end="")
        for arg in args:
           print(arg, end=" ")
        print("")
