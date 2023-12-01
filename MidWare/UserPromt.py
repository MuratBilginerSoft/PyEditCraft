from Utils.Languages.English import Messages as EngMessages
from Utils.Languages.Türkçe import Messages as TrMessages
from MidWare.FindTextSelectLine import FindTextSelectLine
from MidWare.FindTextDeleteLine import FindTextDeleteLine
from MidWare.RemoveTextInFile import RemoveTextInFile
from MidWare.SelectLanguage import SelectLanguage
from MidWare.PrintTerminal import PrintTerminal
from MidWare.ReverseLine import ReverseLine
from MidWare.TxtToExcel import TxtToExcel
from colorama import init, Fore

init(autoreset=True)

class UserPromt:


    # region DocString

    """

    
        
    """

    # endregion

    # region Init
    def __init__(self) -> None:

        self.FindTextSelectLines = FindTextSelectLine()
        self.FindTextDeleteLines = FindTextDeleteLine()
        self.RemoveTextInFiles = RemoveTextInFile()
        self.SelectLanguages = SelectLanguage()
        self.PrintTerminals = PrintTerminal()
        self.ReverseLines = ReverseLine()
        self.TxtToExcels = TxtToExcel()
        
        self.__language = None
        self.__Messages = None
        

    # endregion

    # region Main
    def main(self):

        self.changeLanguage()    
        choice = self.choiceProcess()
        self.process(choice)

    # endregion
    
    # region Change Language    
    def changeLanguage(self):

        self.__language = SelectLanguage.language

        if self.__language == 'English':
            self.__Messages = EngMessages()
        elif self.__language == 'Türkçe':
            self.__Messages = TrMessages()
        else:
            self.__Messages = EngMessages()
    
    # endregion

    # region Choice Process

    def choiceProcess(self):

        print()
        print(Fore.YELLOW + "*" * 50)
        self.PrintTerminals.main("*", Fore.YELLOW)

        self.PrintTerminals.main(f"*   {self.__Messages.messages['1']['message']}",Fore.YELLOW)
        self.PrintTerminals.main("*", Fore.YELLOW)
        self.PrintTerminals.main(f"*   1. {self.__Messages.messages['2']['message']}")
        self.PrintTerminals.main(f"*   2. {self.__Messages.messages['3']['message']}")
        self.PrintTerminals.main(f"*   3. {self.__Messages.messages['4']['message']}")
        self.PrintTerminals.main(f"*   4. {self.__Messages.messages['5']['message']}")
        self.PrintTerminals.main(f"*   5. {self.__Messages.messages['6']['message']}")
        self.PrintTerminals.main(f"*   6. {self.__Messages.messages['18']['message']}", Fore.GREEN)
        self.PrintTerminals.main(f"*   7. {self.__Messages.messages['21']['message']} ", Fore.RED)

        self.PrintTerminals.main("*", Fore.YELLOW)
        
        self.PrintTerminals.main("*" * 50, Fore.YELLOW)
        
        print()

        choice = input(f"{Fore.YELLOW}{self.__Messages.messages['7']['message']} (1,2,3... Select & Enter):")

        return choice

    # endregion

    # region Process
    def process(self, choice):

        if choice == '1':

            targetString = input(self.__Messages.messages['8']['message'])
            sourceFile = input(self.__Messages.messages['9']['message'])
            destinationFile = input(self.__Messages.messages['10']['message'])
            self.FindTextSelectLines.main(targetString, sourceFile, destinationFile)

            print(self.__Messages.messages['17']['message'])
            self.main()

        elif choice == '2':

            targetString = input(self.__Messages.messages['11']['message'])
            fileName = input(self.__Messages.messages['12']['message'])
            self.FindTextDeleteLines.main(fileName, targetString)

            print(self.__Messages.messages['17']['message'])
            self.main()
        
        elif choice == '3':

            targetString = input(self.__Messages.messages['11']['message'])
            fileName = input(self.__Messages.messages['12']['message'])
            self.RemoveTextInFiles.main(fileName, targetString)

            print(self.__Messages.messages['17']['message'])
            self.main()

        elif choice == '4':

            fileName = input(self.__Messages.messages['12']['message'])
            self.ReverseLines.main(fileName)
            print(self.__Messages.messages['17']['message'])
            self.main()
        
        elif choice == '5':
            
            txtFile = input(self.__Messages.messages['14']['message'])
            excelFile = input(self.__Messages.messages['15']['message'])
            self.TxtToExcels.main(txtFile, excelFile)
            print(self.__Messages.messages['17']['message'])
            self.main()

        elif choice == '6':

            self.SelectLanguages.main()
            self.main()

        else:
            print()
            self.PrintTerminals.main(f"{self.__Messages.messages['23']['message']} ", Fore.RED)
    
    # endregion