def play_game():
    is_playing = True
    board = create_game_board()
    is_player_1_turn = True

    while is_playing:
        print(f'Current player: {"Player 1 - X" if is_player_1_turn else "Player 2 - O"}')
        print(board)
        sign = "X" if is_player_1_turn else "O"
        location = get_sign_location_from_user()

        is_player_1_turn = not is_player_1_turn


def create_game_board():
    return '''
       |   |   
    -----------
       |   |   
    -----------
       |   |   
    '''


def get_sign_location_from_user():
    prompt = input("Provide where to write your sign. Only numbers 1 - 9 accepted. (Going from left to right).\n")
    location = int(prompt)
    if 1 <= location <= 9:
        return location
    else:
        print('Not a correct value. Try again.')
        get_sign_location_from_user()


def create_piece_container():
    return [''] * 9


def reset_game():
    pass


if __name__ == '__main__':
    play_game()
