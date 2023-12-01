import json

from Utils.Languages.English import Messages as EngMessages
from Utils.Languages.Türkçe import Messages as TrMessages
from MidWare.PrintTerminal import PrintTerminal
from colorama import init, Fore

init(autoreset=True)
class SelectLanguage:

    language = None

    def __init__(self):
        
        self.__pyConfigPath = 'Utils/Config/PyConfig.json'
        self.PrintTerminals = PrintTerminal()   


    def main(self):

        if SelectLanguage.language == 'English':
            self.__Messages = EngMessages()
            self.__endMessage = "Invalid choice..."
        elif SelectLanguage.language == 'Türkçe':
            self.__Messages = TrMessages()
            self.__endMessage = "Geçersiz seçim..."
        else:
            self.__Messages = EngMessages()
            self.__endMessage = "Invalid choice..."

        print()
        print(Fore.YELLOW + "*" * 50)
        self.PrintTerminals.main("*", Fore.YELLOW)
        self.PrintTerminals.main(f"*   {self.__Messages.messages['20']['message']}",Fore.YELLOW)
        self.PrintTerminals.main("*", Fore.YELLOW)
        self.PrintTerminals.main(f"*   1. English", Fore.BLUE)
        self.PrintTerminals.main(f"*   2. Türkçe", Fore.MAGENTA)

        self.PrintTerminals.main("*", Fore.YELLOW)
        
        self.PrintTerminals.main("*" * 50, Fore.YELLOW)

        print()

        choice = input(f"{Fore.YELLOW}{self.__Messages.messages['22']['message']} (1,2... Select & Enter):")

        if choice == '1':

            self.setLanguageJson('English')

        elif choice == '2':

            self.setLanguageJson('Türkçe')

        else:
            print(self.__endMessage)

    def setLanguageJson(self, language):

        with open(self.__pyConfigPath, 'r+', encoding='utf-8') as f:
            
            data = json.load(f)
            data['language'] = language  
            f.seek(0) 
            json.dump(data, f, indent=4, ensure_ascii=False)  
            f.truncate()
        
        SelectLanguage.language = language
        print(SelectLanguage.language)