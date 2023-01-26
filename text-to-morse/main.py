import re

alpha_morse_dict = {
    'a': '•-',
    'b': '-•••',
    'c': '-•-•',
    'd': '-••',
    'e': '•',
    'f': '••-•',
    'g': '--•',
    'h': '••••',
    'i': '••',
    'j': '•---',
    'k': '-•-',
    'l': '•-••',
    'm': '--',
    'n': '-•',
    'o': '---',
    'p': '•--•',
    'q': '--•-',
    'r': '•-•',
    's': '•••',
    't': '-',
    'u': '••-',
    'v': '•••-',
    'w': '•--',
    'x': '-••-',
    'y': '-•--',
    'z': '--••',
    '1': '•----',
    '2': '••---',
    '3': '•••---',
    '4': '••••-',
    '5': '•••••',
    '6': '-••••',
    '7': '--•••',
    '8': '---••',
    '9': '----•',
    '0': '-----'
}


def main():
    keep_prompting = True
    while keep_prompting:
        user_input = prompt_user()
        morse = convert_user_input(user_input)
        print(f'The morse equivalent it: {morse}')


def prompt_user():
    return input('Provide a text to convert to morse code.\n').lower()


def convert_user_input(user_input):
    user_input = clean_input(user_input)
    morse = ''
    for char in user_input:
        if char == ' ':
            morse += char
        else:
            morse += alpha_morse_dict[char]
    return morse


def clean_input(user_input):
    user_input = user_input.lower()
    user_input = re.sub(r'[^a-zA-Z0-9\s]', ' ', user_input)
    user_input = re.sub(r'\s(?=\s)', '', user_input)
    return user_input


if __name__ == '__main__':
    main()
