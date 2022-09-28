# -*- coding: utf-8 -*-

SUMMATOR_CONFIG = {
    '{': {
        'key': '{}',
        'weight': 1,
    },
    '}': {
        'key': '{}',
        'weight': -1,
    },
    '[': {
        'key': '[]',
        'weight': 1,
    },
    ']': {
        'key': '[]',
        'weight': -1,
    },
    '(': {
        'key': '()',
        'weight': 1,
    },
    ')': {
        'key': '()',
        'weight': -1,
    },
}


def check_str(input_str, summator_config):
    print(input_str)

    summator = {}
    for conf_key, conf_item in summator_config.items():
        summator[conf_item['key']] = 0

    for symbol in input_str:
        if symbol in summator_config:
            summator[summator_config[symbol]['key']] += summator_config[symbol]['weight']
            if summator[summator_config[symbol]['key']] < 0:
                return False

    for key in summator:
        if summator[key] != 0:
            return False
    return True


if __name__ == '__main__':
    input_strings = [
        '[[({}}])]',
        '[[({}])]',
        '[[({}][[[])}{})((])]'
    ]

    for input_str in input_strings:
        print(check_str(input_str, SUMMATOR_CONFIG))
