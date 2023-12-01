class FindTextSelectLine:

    # region DocString

    """
    
    This module contains the functionality to manipulate text files. 

    It includes functions to read from a file, find specific text, and delete lines. 

    The main function orchestrates these operations based on user input.

    Usage:
    
        import FindTextDeleteLine
        FindTextDeleteLine.main()
        
    """

    # endregion

    # region Init

    def __init__(self) -> None:
        pass

    # endregion

    # region Main

    def main(self, targetString, sourceFile, destinationFile):
        
        with open(sourceFile, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        matching_lines = [line for line in lines if targetString in line]

        with open(destinationFile, 'w', encoding='utf-8') as file:
            for line in matching_lines:
                file.write(line)
    
    # endregion