class ReverseLine:

    # region Init

    def __init__(self) -> None:
        pass

    # endregion

    # region Main

    def main(self, fileName):
        
        with open(fileName, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        reversedLines = lines[::-1]

        with open(fileName, 'w', encoding='utf-8') as file:
            file.writelines(reversedLines)
    
    # endregion