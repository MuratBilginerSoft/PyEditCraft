import json

class ReadLanguageJson:

    # region DocString

    """

    This module contains the ReadLanguageJson class which is used to read the language setting from a JSON configuration file.

    The main method of the class opens the configuration file, reads the JSON data, and returns the current language setting.

    """

    # endregion

    # region Init
    def __init__(self):

        self.__language = None
        self.__pyConfigPath = 'Utils/Config/PyConfig.json'

    # endregion
    
    # region Main 
    def main(self):

        with open(self.__pyConfigPath, 'r', encoding="utf-8") as f:
            data = json.load(f)
            self.__language = data.get('language', '')

        return self.__language

    # endregion