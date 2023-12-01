import pandas as pd

class TxtToExcel:

    # region DocString

    """

    This module, TxtToExcel, is responsible for converting text files to Excel files.

    The main function in this module reads a text file, converts it into a DataFrame using pandas, and then writes that DataFrame to an Excel file.

    Usage:
        import TxtToExcel
        converter = TxtToExcel()
        converter.main("example.txt", "output.xlsx")
        
    """

    # endregion

    # region Init

    def __init__(self) -> None:
        pass

    # endregion

    # region Main

    def main(self, txtFile, excelFile):
        
        df = pd.read_csv(txtFile, delimiter = "\t")
        df.to_excel(excelFile, index=False)
    
    # endregion