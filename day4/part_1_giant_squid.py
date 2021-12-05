# Import custom class
import bingo_functions as bf

# Reading in data
with open(".\input.txt") as f:
    data = f.readlines()

# Parsing all the input numbers
input_nums = [int(x) for x in data[0].strip().split(",")]

# Creating a flag to indicate a new board
new_board = 0
# Creating a list to store all boards as they are defined (in order)
all_boards = []

# Iterating over remaning data which are the boards
for i, line in enumerate(data[2:]):
    if not new_board:
        # Set new board to 1
        new_board = 1
        # Append current line a new variable 'curr_board'
        # Split numbers into list of integers and append as list i.e.
        # curr_board = [[a,b,c...,e]]
        curr_board = [[int(x) for x in line.strip().split(" ") if x != ""]]
    # New line indicates curr board has finished and ensuring old board is in
    # progress (i.e. new_board = 1)
    elif line == "\n" and new_board:
        # Set new_board flag to 0 to indicate we have finished the board
        new_board = 0
        # Append the finished board to the all_boards list as a Board class
        all_boards.append(bf.Board(curr_board))
    # Else, this is another line to the current board so append to curr_board
    # in same format as clause 1 i.e. list of ints
    else:
        curr_board.append([int(x) for x in line.strip().split(" ") if x != ""])

# This appends the last board to the all_boards list
all_boards.append(bf.Board(curr_board))


print("Playing Bingo!\n\n")

# Defining a main function
def main(input_nums, all_boards):
    # Iterating over all input numbers
    for input_num in input_nums:
        print(f"Input: {input_num}")
        # Iterating over all boards
        for i, board in enumerate(all_boards):
            # For current board, check if input_num is a hit
            board.check_hit(input_num)
            # Check if, after hit, a win condition is met on board
            row_check = board.check_win_row()
            col_check = board.check_win_col()

            # If neither row or col is a 'win', move on
            if row_check == None and col_check == None:
                continue
            else:
                # Else return the board number and the input_num
                return i, input_num


# Calling main
board_num, input_to_win = main(input_nums, all_boards)
print(f"Winner! Board: {board_num} on Number: {input_to_win}")

# curr_df is the manipulated df for curr board
curr_df = all_boards[board_num].df
# Need to (-1) for all nums to correct for initial change
curr_df = (curr_df[curr_df != 0] - 1).fillna(0)
# Getting a sum of all rows and then sum of that - gives total sum
unmarked_nums = curr_df.sum().sum()
# Print result
print(int(unmarked_nums * input_to_win))
