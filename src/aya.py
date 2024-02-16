import datetime
import inspect

class TextColor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'

class Template:
    def __init__(self, raw):
        self.raw = raw
    def verify_raw(self):
        """
        Input Keywords
        {TIME} A timestamp of the time the log was called
        {DATE} The day the log was called
        {TYPE} The type of log that was called
        {LINE} 
        {LOGFILE}
        {FILE}
        """
        replaced = self.raw.replace("{TIME}", "")\
            .replace("{DATE}", "")\
            .replace("{TYPE}", "")\
            .replace("{LINE}", "")\
            .replace("{LOGFILE}", "")\
            .replace("{FILE}", "")\
            .replace("{MSG}", "")
        if "{" in replaced or "}" in replaced:
            return False
        else:
            return True
        
                

class Logger:
    def __init__(self, template=None, logfile=None):
        self.logfile = logfile
        self.template = Template(template)

    def debug(self, msg):
        if self.template is not None:
            if self.template.verify_raw():
                raw = self.template.raw
                current_time = datetime.datetime.now()
                DATE = current_time.strftime("%Y-%m-%d")
                TIME = current_time.strftime("%H:%M:%S")
                TYPE = "DEBUG"
                LINE = inspect.currentframe().f_back.f_lineno
                LOGFILE = self.logfile
                FILE = __file__
                printed = raw.replace("{DATE}", str(DATE)).replace("{TIME}", str(TIME)).replace("{TYPE}", str(TYPE)).replace("{LINE}", str(LINE)).replace("{LOGFILE}", str(LOGFILE)).replace("{FILE}", str(FILE)).replace("{MSG}", str(msg))
                print(printed)

            else:
                raise SyntaxError
        else:
            printed = msg
            print(printed)
                
        if self.logfile is not None:
            with open(self.logfile, "a") as f:
                f.write(printed + "\n")
        

    def info(self, msg):
        if self.template is not None:
            if self.template.verify_raw():
                raw = self.template.raw
                current_time = datetime.datetime.now()
                DATE = current_time.strftime("%Y-%m-%d")
                TIME = current_time.strftime("%H:%M:%S")
                TYPE = "INFO"
                LINE = inspect.currentframe().f_back.f_lineno
                LOGFILE = self.logfile
                FILE = __file__
                printed = raw.replace("{DATE}", str(DATE)).replace("{TIME}", str(TIME)).replace("{TYPE}", str(TYPE)).replace("{LINE}", str(LINE)).replace("{LOGFILE}", str(LOGFILE)).replace("{FILE}", str(FILE)).replace("{MSG}", f"{TextColor.GREEN}{msg}{TextColor.RESET}")
                print(printed)

            else:
                raise SyntaxError
        else:
            printed = msg
            print(printed)
                
        if self.logfile is not None:
            with open(self.logfile, "a") as f:
                f.write(printed.replace(TextColor.GREEN, "").replace(TextColor.RESET, "") + "\n")
    

    def warn(self, msg):
        if self.template is not None:
            if self.template.verify_raw():
                raw = self.template.raw
                current_time = datetime.datetime.now()
                DATE = current_time.strftime("%Y-%m-%d")
                TIME = current_time.strftime("%H:%M:%S")
                TYPE = "WARNING"
                LINE = inspect.currentframe().f_back.f_lineno
                LOGFILE = self.logfile
                FILE = __file__
                printed = raw.replace("{DATE}", str(DATE)).replace("{TIME}", str(TIME)).replace("{TYPE}", str(TYPE)).replace("{LINE}", str(LINE)).replace("{LOGFILE}", str(LOGFILE)).replace("{FILE}", str(FILE)).replace("{MSG}", f"{TextColor.YELLOW}{msg}{TextColor.RESET}")
                print(printed)

            else:
                raise SyntaxError
        else:
            printed = msg
            print(printed)
                
        if self.logfile is not None:
            with open(self.logfile, "a") as f:
                f.write(printed.replace(TextColor.YELLOW, "").replace(TextColor.RESET, "") + "\n")
    

    def error(self, msg):
        if self.template is not None:
            if self.template.verify_raw():
                raw = self.template.raw
                current_time = datetime.datetime.now()
                DATE = current_time.strftime("%Y-%m-%d")
                TIME = current_time.strftime("%H:%M:%S")
                TYPE = "ERROR"
                LINE = inspect.currentframe().f_back.f_lineno
                LOGFILE = self.logfile
                FILE = __file__
                printed = raw.replace("{DATE}", str(DATE)).replace("{TIME}", str(TIME)).replace("{TYPE}", str(TYPE)).replace("{LINE}", str(LINE)).replace("{LOGFILE}", str(LOGFILE)).replace("{FILE}", str(FILE)).replace("{MSG}", f"{TextColor.RED}{msg}{TextColor.RESET}")
                print(printed)

            else:
                raise SyntaxError
        else:
            printed = msg
            print(printed)
                
        if self.logfile is not None:
            with open(self.logfile, "a") as f:
                f.write(printed.replace(TextColor.RED, "").replace(TextColor.RESET, "") + "\n")
    

    def critical(self, msg):
        if self.template is not None:
            if self.template.verify_raw():
                raw = self.template.raw
                current_time = datetime.datetime.now()
                DATE = current_time.strftime("%Y-%m-%d")
                TIME = current_time.strftime("%H:%M:%S")
                TYPE = "CRITICAL"
                LINE = inspect.currentframe().f_back.f_lineno
                LOGFILE = self.logfile
                FILE = __file__
                printed = raw.replace("{DATE}", str(DATE)).replace("{TIME}", str(TIME)).replace("{TYPE}", str(TYPE)).replace("{LINE}", str(LINE)).replace("{LOGFILE}", str(LOGFILE)).replace("{FILE}", str(FILE)).replace("{MSG}", f"{TextColor.MAGENTA}{msg}{TextColor.RESET}")
                print(printed)

            else:
                raise SyntaxError()
        else:
            printed = msg
            print(printed)
                
        if self.logfile is not None:
            with open(self.logfile, "a") as f:
                f.write(printed.replace(TextColor.MAGENTA, "").replace(TextColor.RESET, "") + "\n")


if __name__ == "__main__":
    mylog = Logger(template="{DATE} {TIME} {FILE}:{LINE} - {TYPE}: {MSG}", logfile="test.txt")
    mylog.debug("This is a debug message")
    mylog.info("This is a info message")
    mylog.warn("This is a warning message")
    mylog.error("This is an error message")
    mylog.critical("This is a critical message")
    print("This is a normal print")
    mylog.debug("New Demo")
