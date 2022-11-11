colorcodes: dict[str, str] = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "normal": "\033[0m",
        "bold": "\033[1m",
        "underscore": "\033[4m",
        "blink": "\033[5m",
        "reverse": "\033[7m",
        "conceal": "\033[8m",
    }
def colorize(text: str, color: str) -> str:
    """
    Colorize text.
    """
    

    return f"{colorcodes[color]}{text}\033[0m"

class Colorizer:
    __COLORS = ""
    def red(self, text):
        self.__COLORS = f"{self.__COLORS}\033[31m{text}"
        return self
    def green(self, text):
        self.__COLORS = f"{self.__COLORS}\033[32m{text}"
        return self
    def blue(self, text):
        self.__COLORS = f"{self.__COLORS}\033[34m{text}"
        return self
    def magenta(self, text):
        self.__COLORS = f"{self.__COLORS}\033[35m{text}"
        return self
    def cyan(self, text):
        self.__COLORS = f"{self.__COLORS}\033[36m{text}"
        return self
    def white(self, text):
        self.__COLORS = f"{self.__COLORS}\033[37m{text}"
        return self
    def normal(self, text):
        self.__COLORS = f"{self.__COLORS}\033[0m{text}"
        return self
    def bold(self, text):
        self.__COLORS = f"{self.__COLORS}\033[1m{text}"
        return self
    def underscore(self, text):
        self.__COLORS = f"{self.__COLORS}\033[4m{text}"
        return self
    def blink(self, text):
        self.__COLORS = f"{self.__COLORS}\033[5m{text}"
        return self
    def reverse(self, text):
        self.__COLORS = f"{self.__COLORS}\033[7m{text}"
        return self
    def conceal(self, text):
        self.__COLORS = f"{self.__COLORS}\033[8m{text}"
        return self
    def resolve(self):
        return self.__COLORS + "\033[0m"
def create_colorizer():  return Colorizer()
