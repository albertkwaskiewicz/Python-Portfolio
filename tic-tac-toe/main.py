import math

def play_game():
    is_playing = True
    board = create_game_board()
    is_player_1_turn = True
    signs_container = create_sign_container()
    print(board)

    while is_playing:
        print(f'Current player: {"Player X" if is_player_1_turn else "Player O"}')
        sign = "X" if is_player_1_turn else "O"

        board = assign_sign(sign, signs_container)
        print(board)

        is_game_over(signs_container)

        is_player_1_turn = not is_player_1_turn


def create_game_board():
    new_board = ''
    split = '-----------'
    for num in range(1, 10):
        if num % 3 == 0:
            new_board += f'   |   |   \n'
            if num != 9:
                new_board += f'{split}\n'
    return new_board


def create_sign_container():
    num_rows = 3
    return [[' ', ' ', ' '] for _ in range(num_rows)]


def assign_sign(sign, container: list):
    location = get_sign_location_from_user()
    row_size = 3
    row = math.ceil(location / row_size) - 1
    index = 2 if location % row_size == 0 else (location % row_size - 1)

    if container[row][index] == ' ':
        container[row][index] = sign
        return update_board(container)
    else:
        print("\nThat spot is already taken: Try again.")
        assign_sign(sign, container)


def get_sign_location_from_user():
    prompt = input("Provide where to write your sign. Only numbers 1 - 9 accepted. (Going from left to right).\n")
    location = int(prompt)
    if 1 <= location <= 9:
        return location
    else:
        print('Not a correct value. Try again.')
        get_sign_location_from_user()


def update_board(container):
    new_board = ''
    split = '-----------'

    for index, row in enumerate(container):
        new_board += f' {row[0]} | {row[1]} | {row[2]} \n'
        if (index + 1) != len(container):
            new_board += f'{split}\n'
    return new_board


def is_game_over(sign, collection):
    for row in collection:
        pass
    if '' not in collection:
        return True


def reset_game():
    pass


if __name__ == '__main__':
    play_game()
