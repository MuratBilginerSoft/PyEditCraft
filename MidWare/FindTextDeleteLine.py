class FindTextDeleteLine:

    # region Init

    def __init__(self) -> None:
        pass

    # endregion

    # region Main

    def main(self, fileName, targetString):

        with open(fileName, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        linesToKeep = [line for line in lines if targetString not in line]

        with open(fileName, 'w', encoding='utf-8') as file:
            file.writelines(linesToKeep)
    
    # endregion