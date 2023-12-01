from colorama import init, Fore, Style
class PrintTerminal:

    def __init__(self):
        pass

    def main(self, message, color=Fore.RESET):

        message = message.ljust(50)
        message = message[:49] + '*' + message[50:]
        print(color + message)