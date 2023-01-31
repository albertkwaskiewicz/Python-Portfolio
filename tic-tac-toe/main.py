def play_game():
    is_playing = True
    board = create_game_board()
    is_player_1_turn = True
    signs_container = create_sign_container()
    print(board)

    while is_playing:
        print(f'Current player: {"Player 1 - X" if is_player_1_turn else "Player 2 - O"}')
        sign = "X" if is_player_1_turn else "O"

        board = assign_sign(sign, signs_container)
        print(board)

        is_player_1_turn = not is_player_1_turn


def create_game_board():
    new_board = ''
    split = '---------'
    for num in range(1, 10):
        if num % 3 == 0:
            new_board += f'  |  |  \n'
            if num != 9:
                new_board += f'{split}\n'
    return new_board


def create_sign_container():
    return [''] * 9


def assign_sign(sign, container: list):
    location = get_sign_location_from_user()
    index = location - 1
    if container[index] == '':
        del container[index]
        container.insert(index, sign)
        return update_board(container)
    else:
        print("That spot is already taken: Try again.")
        assign_sign(sign, container)


def get_sign_location_from_user():
    prompt = input("Provide where to write your sign. Only numbers 1 - 9 accepted. (Going from left to right).\n")
    location = int(prompt)
    if 1 <= location <= 9:
        return location
    else:
        print('Not a correct value. Try again.')
        get_sign_location_from_user()


# TODO: Improve func so lines are always aligned
def update_board(container):
    new_board = ''
    split = '---------'

    for index, _ in enumerate(container):
        if (index + 1) % 3 == 0:
            new_board += f' {container[index - 2]} | {container[index - 1]} | {container[index]} \n'
            if (index + 1) != len(container):
                new_board += f'{split}\n'
    return new_board


def is_game_over():
    pass


def reset_game():
    pass


if __name__ == '__main__':
    play_game()
