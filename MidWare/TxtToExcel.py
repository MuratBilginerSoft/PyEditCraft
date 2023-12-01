import pandas as pd

class TxtToExcel:

    # region Init

    def __init__(self) -> None:
        pass

    # endregion

    # region Main

    def main(self, txtFile, excelFile):
        
        df = pd.read_csv(txtFile, delimiter = "\t")
        df.to_excel(excelFile, index=False)
    
    # endregion