from helpers import get_players_chosen_position
from chars import full_large_mapping, row_divider, board_width

square_num = 3
board_structure = [["", "", ""] for _ in range(square_num)]


letter_width = board_width//3 + 1


def generate_large_letters(first, second, third, row_num: int):


    print_num = False
    for i in range(len(full_large_mapping["X"])):
        if i == len(full_large_mapping["X"]) // 2:
            print_num = True
        print(row_num if print_num else " ", full_large_mapping[first][i], " ", full_large_mapping[second][i], " ", full_large_mapping[third][i])
        print_num = False



def generate_board():
    print("1".center(letter_width), "2".center(letter_width), "3".center(letter_width - 2))
    print(" ", row_divider)
    for row_num in range(len(board_structure)):
        strings = []

        for column_num in range(len(board_structure[row_num])):
            column = board_structure[row_num][column_num]
            if column == "":
                strings.append("EMPTY")
            else:
                strings.append(column)

        generate_large_letters(*strings, row_num+1)
    print(" ", row_divider)


def check_all():
    player_dict = {
        "X": {
            # "diagonal1": 0,
            # "diagonal2": 0,

        },
        "O": {
            # "diagonal1": 0,
            # "diagonal2": 0
        }
    }


    # def diagonal(row_num, row_val, col_num, col_val):
    #     nonlocal player_dict
    #     difference = row_num - col_num
    #     if row_num == 0 and col_num == 0:
    #         player_dict[col_val]["diagonal1"] = 0
    #         player_dict[col_val]["diagonal2"] = 0
    #
    #     if row_num == col_num:
    #         if row_num == abs(square_num-1):
    #             player_dict[col_val]["diagonal1"] += 1
    #             player_dict[col_val]["diagonal2"] += 1
    #
    #     elif difference == square_num - 1 or difference == (square_num - 1)*-1:
    #         player_dict["diagonal2"] += 1
    #
    #     if player_dict[col_val]["diagonal"] == 3:
    #         return True
    #
    #
    # def row(row_num, row_val, col_num, col_val):
    #     nonlocal player_dict
    #     player_dict[col_val]["row"] += 1
    #     if player_dict[col_val]["row"] == 3:
    #         return col_val
    #
    #     player_dict = {"X": {}, "Y": {}}
    #
    # def col(row_num, row_val, col_num, col_val):
    #     nonlocal player_dict
    #     player_dict[col_val]["row"] += 1
    #     if player_dict[col_val]["row"] == 3:
    #         return col_val
    #
    #
    # diagonal_winner = sift_cells(diagonal)
    # if diagonal_winner:
    #     return diagonal_winner
    #
    # row_winner = sift_cells(row)
    # if row_winner:
    #     return row_winner
    #
    # col_winner = sift_cells(col)
    # if col_winner:
    #     return col_winner


def get_col_row_winner(board: list[list], row_or_column: str):
    for row_num, row in enumerate(board):
        row_match_dict = {}
        for col_num, col in enumerate(row):
            if col != "":
                player = col
                already_counted = row_match_dict.get(player)

                if already_counted:
                    row_match_dict[player] += 1
                else:
                    row_match_dict[player] = 1
                # print(f"{row_or_column.upper()} MATCH DICT: ", row_match_dict)
                if player and row_match_dict[player] == 3:
                    return player, row_or_column.upper(), row_num

    return False, False, False


def win_logic():
    transposed_board = [[board_structure[j][i] for j in range(len(board_structure))] for i in range(len(board_structure[0]))]
    diagonal_match_dict = {}
    for index, element in enumerate(board_structure):
        if board_structure[index][index] == transposed_board[index][index]:
            if element[index] != "":
                if diagonal_match_dict.get(element[index]):
                    diagonal_match_dict[element[index]] += 1
                else:
                    diagonal_match_dict[element[index]] = 1


    print("DIAGONAL MATCH DICT: ", diagonal_match_dict)
    print("BOARD STRUCTURE: ", board_structure)
    print("TRANSPOSED BOARD: ", transposed_board)

    diagonal_winner = [x for x in diagonal_match_dict.keys() if diagonal_match_dict[x] == 3 and x != ""]
    diagonal_win_type = False
    if len(diagonal_winner) > 0:
        diagonal_win_type = "BOTTOM-LEFT TO TOP-RIGHT" if transposed_board[0][0] == diagonal_winner \
            else "TOP-LEFT TO BOTTOM-RIGHT"



    row_winner, row_text, row_number = get_col_row_winner(board_structure, "ROW")


    column_winner, column_text, column_number = get_col_row_winner(transposed_board, "COLUMN")


    if (diagonal_winner and (row_winner or column_winner)) or row_winner and column_winner:
        win_text = "DOUBLE WIN!"
        if diagonal_winner and row_winner:
            double_winner = row_winner
            win_type = win_text + f" ROW: {row_number} and DIAGONAL: {diagonal_win_type}"
            print(win_type)
            return double_winner, win_type, row_number

        if row_winner and column_winner:
            double_winner = row_winner
            win_type = win_text + f" ROW: {row_number} and COLUMN: {column_number}"
            print(win_type)
            return double_winner, win_type, row_number

        if column_winner and diagonal_winner:
            double_winner = column_winner
            win_type = win_text + f" COLUMN: {column_number} and DIAGONAL: {diagonal_win_type}"
            print(win_type)
            return double_winner

    else:
        if diagonal_winner:
            print(f"Player {diagonal_winner[0]} Wins DIAGONAL: {diagonal_win_type}!")
            return diagonal_winner[0]

        if row_winner:
            print(f"Player {row_winner} Wins {row_text}: {row_number+1}!")
            return row_winner

        if column_winner:
            print(f"Player {column_winner} Wins {column_text}: {column_number+1}!")
            return column_winner

    return False


def play_tic_tac_toe():
    num_tics = 100
    tic_tac_toe = " Tic Tac Toe ".center(num_tics, "=")
    print("=" * num_tics)
    print(tic_tac_toe)
    print("=" * num_tics)
    print()
    print()
    generate_board()
    for turn in range((square_num**2)+1):
        for player_num in range(2):
            if player_num == 0:
                player_string = "X"
            elif player_num == 1:
                player_string = "O"
            else:
                raise ValueError("Too Many Turns Are Being Used")

            while True:
                loc = get_players_chosen_position(player_string)
                if loc:
                    x, y = loc
                    if board_structure[y][x] == "":
                        board_structure[y][x] = player_string
                        generate_board()
                        winner = win_logic()
                        if winner:
                            # print(f"Player {winner} Wins {win_type}: {sub}!")
                            return
                        break
                    else:
                        print("That Spot Is Already Taken, Pick Another Spot")
                        continue
                else:
                    print("Uh-oh Something Went wrong! :<")

                # player_turns[i].append(loc)


play_tic_tac_toe()
