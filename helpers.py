def out_of_bounds_message(player_letter: str, chosen_number: int, problem: str = ">"):
    if problem == ">":
        print(f"The number: {chosen_number} for player {player_letter} Is Too Large")
    else:
        print(f"The number: {chosen_number} for player {player_letter} Is Too Small")
    print("Please Enter A Number Between 1 and 3")



def choice_is_acceptable(choice, player_letter, numbers):
    if choice > 3:
        out_of_bounds_message(player_letter, choice)
        return False
    elif choice < 1:
        out_of_bounds_message(player_letter, choice, "<")
        return False
    else:
        if len(numbers) == 0 or len(numbers) == 1:
            if isinstance(choice, str):
                raise ValueError("The Choice Is Still A String")
            else:
                return True


def get_players_chosen_position(player_letter: str) -> tuple | bool:
    choices = []
    print(f"Player {player_letter}'s Turn")
    while len(choices) < 2:
        choice = take_input(choices)
        if choice and choice_is_acceptable(choice, player_letter, choices):
            choice -= 1
            choices.append(choice)
        if len(choices) == 2:
            choices = tuple(choices)
    return choices



def take_input(numbers):
    choice = input(f"{'X' if len(numbers) == 0 else 'Y'} Location: \n")
    try:
        choice = int(choice)
        return choice
    except ValueError:
        print(f"Your Choice Of {choice} Is Not A Number Between 1 and 3")
        return False



