# -*- coding: utf-8 -*-

def sum_bin(x1, x2):
    dec_x1 = int(x1, 2)
    dec_x2 = int(x2, 2)
    print(f'X1: {x1} ({dec_x1})')
    print(f'X2: {x2} ({dec_x2})')
    dec_res = dec_x1 * dec_x2
    return (bin(dec_res)[2:], dec_res)


if __name__ == '__main__':
    input_pairs = [
        ('1101101001', '1101011'),
        ('1100101', '11011'),
        ('11', '110011')
    ]

    for input_pair in input_pairs:
        res = sum_bin(input_pair[0], input_pair[1])
        print(f'Sum: {res[0]} ({res[1]})')
