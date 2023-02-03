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

        if is_game_over(sign, signs_container):
            print('Game Over!')
            keep_playing = input('Would you like to play again? Y/N\n').lower()
            if keep_playing != 'y':
                print('Thanks for playing! Until next time!')
                is_playing = not is_playing
            else:
                play_game()

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
        return get_sign_location_from_user()


def update_board(container):
    new_board = ''
    split = '-----------'

    for index, row in enumerate(container):
        new_board += f' {row[0]} | {row[1]} | {row[2]} \n'
        if (index + 1) != len(container):
            new_board += f'{split}\n'
    return new_board


def is_game_over(sign, container):
    return did_player_win(sign, container) or is_container_full(container)


def did_player_win(sign, container):
    if is_row_match(sign, container) or is_column_match(sign, container) or is_diagonal_match(sign, container):
        print(f'Player {sign} wins! Congrats!')
        return True


def is_row_match(sign, container):
    for row in container:
        if all(item == sign for item in row):
            return True


def is_column_match(sign, container):
    row_size = 3
    column_values = []
    for index in range(row_size):
        for row in container:
            column_values.append(row[index])
        if all(item == sign for item in column_values):
            return True
        column_values = []
    return False


def is_diagonal_match(sign, container):
    diagonal_values = get_diagonals(container)
    if all(item == sign for item in diagonal_values):
        return True

    diagonal_values = get_diagonals(reversed(container))
    if all(item == sign for item in diagonal_values):
        return True

    return False


def get_diagonals(container):
    diagonal_values = []
    i = 0
    for row in container:
        diagonal_values.append(row[i])
        i += 1
    return diagonal_values


def is_container_full(container):
    flat_container = [sign for row in container for sign in row]
    if ' ' not in flat_container:
        return True


if __name__ == '__main__':
    play_game()
