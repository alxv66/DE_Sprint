# -*- coding: utf-8 -*-

ROMAN_CODER_CONFIG = {
    'ones': ["","I","II","III","IV","V","VI","VII","VIII","IX"],
    'tens': ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
    'hundreds': ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
    'thousands': ["","M","MM"],
}


def arab_to_roman(arab, coder_config):
    print(arab)
    rom = coder_config['thousands'][arab // 1000] + \
          coder_config['hundreds'][arab // 100 % 10] + \
          coder_config['tens'][arab // 10 % 10] + \
          coder_config['ones'][arab  % 10]

    return rom


if __name__ == '__main__':
    input_arabs = [
        3,
        9,
        15,
        296,
        10,
        1984,
        1945,
        2022
    ]

    for input_arab in input_arabs:
        print(arab_to_roman(input_arab, ROMAN_CODER_CONFIG))
