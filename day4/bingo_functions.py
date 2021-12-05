# Import
import pandas as pd


# Defining board class
class Board:
    # Create df from curr board list of lists
    def __init__(self, board_list):
        # Creating a df
        self.df = pd.DataFrame(board_list)
        # Keeping a copy to have the base, unchanged values
        self.orig = self.df.copy()
        # Adding 1 to every element so no '0' exists in the board
        self.df = self.df + 1

    def check_hit(self, value):
        # Adding 1 to the value to calibrate with the df that has 1 added to it
        value = value + 1

        # Checking where in the df that value exists. This will return a df
        # mask where 'True' is where no match is and 'False' is with a match
        mask = pd.isnull(self.df[self.df == value])

        # Assigning all the 'False' values in the mask with a 0 to indicate
        # it has been hit
        self.df[~mask] = 0

    def check_win_row(self):
        # sum of all rows
        row_check = list(self.df.sum(axis=1))
        # If any of the sums equal 0
        if 0 in row_check:
            # Return that row index
            return row_check.index(0)
        else:
            # Else return None
            return None

    def check_win_col(self):
        # sum of all columns
        col_check = list(self.df.sum(axis=0))
        # If any of the sums equal 0
        if 0 in col_check:
            # Return that col index
            return col_check.index(0)
        else:
            # Else return None
            return None
