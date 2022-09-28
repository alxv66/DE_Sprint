# -*- coding: utf-8 -*-

def is_palindrom(input_str):
    print(input_string)
    no_spaces_str = input_str.replace(' ', '')
    for i in range(len(no_spaces_str)//2):
        if (no_spaces_str[i] != no_spaces_str[-i-1]):
            return False

    return True


if __name__ == '__main__':
    input_strings = [
        'taco cat',
        'rotator',
        'black cat',
        'а роза упала на лапу азора'
    ]

    for input_string in input_strings:
        print(is_palindrom(input_string))
