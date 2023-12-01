class RemoveTextInFile:

    # region Init

    def __init__(self) -> None:
        pass

    # endregion

    # region Main

    def main(self, fileName, targetString):
        
        with open(fileName, 'r', encoding='utf-8') as file:
            content = file.read()

        content = content.replace(targetString, '')

        with open(fileName, 'w', encoding='utf-8') as file:
            file.write(content)
    
    # endregion