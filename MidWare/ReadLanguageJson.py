import json

class ReadLanguageJson:

    def __init__(self):

        self.__language = None
        self.__pyConfigPath = 'Utils/Config/PyConfig.json'
        
    def main(self):

        with open(self.__pyConfigPath, 'r', encoding="utf-8") as f:
            data = json.load(f)
            self.__language = data.get('language', '')

        return self.__language