class ReverseLine:

    # region DocString

    """

    This module, ReverseLine, is responsible for reversing the lines in a file.

    It provides a function to read a file, reverse the order of lines, and write the result back to the file.

    Usage:
        import ReverseLine
        ReverseLine.reverse_lines("example.txt")

    """

    # endregion

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