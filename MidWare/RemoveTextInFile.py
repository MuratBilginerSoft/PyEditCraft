class RemoveTextInFile:

    # region DocString

    """

    This module, RemoveTextInFile, is responsible for removing specific text from a file.

    It provides a function to read a file, find and remove specific text, and write the result back to the file.

    Usage:
        import RemoveTextInFile
        RemoveTextInFile.remove_text("example.txt", "text to remove")

    """

    # endregion

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