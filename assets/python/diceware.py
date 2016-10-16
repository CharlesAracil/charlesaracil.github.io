"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt


class FlipCoinData(object):
    n_groups = 8
    outcome1 = ('0', '1')
    outcome3 = ('000', '001', '010', '011', '100', '101', '110', '111')

    def __init__(self, data):
        self.data = data
        # number of zeroes and ones
        self.nb01 = (data.count('0'), data.count('1'))
        # groups of 3
        _g3 = [''.join(e) for e in zip(self.data[::3], self.data[1::3], self.data[2::3])]
        self.g3 = []
        for o in FlipCoinData.outcome3:
            self.g3.append(_g3.count(o))


def display_g1(computer, man):
    n_groups = 2
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4

    _ = plt.bar(index, computer.nb01, bar_width,
                alpha=opacity,
                color='b',
                label='computer')

    _ = plt.bar(index + bar_width, man.nb01, bar_width,
                alpha=opacity,
                color='r',
                label='man')

    plt.xlabel('Outcome')
    plt.ylabel('number of outcomes')
    plt.xticks(index + bar_width, ('0', '1'))
    plt.legend()

    plt.tight_layout()
    plt.savefig('diceware_g1.png')


def display_g3(computer, man):
    n_groups = FlipCoinData.n_groups
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4

    _ = plt.bar(index, computer.g3, bar_width,
                alpha=opacity,
                color='b',
                label='computer')

    _ = plt.bar(index + bar_width, man.g3, bar_width,
                alpha=opacity,
                color='r',
                label='man')

    plt.xlabel('Outcome')
    plt.ylabel('number of outcomes')
    plt.xticks(index + bar_width, FlipCoinData.outcome3)
    plt.legend()

    plt.tight_layout()
    plt.savefig('diceware_g3.png')

if __name__ == '__main__':
    # data just for dev debug
    _dataA_raw = '000001010011100101110111'
    _dataB_raw = '000111000111000111000111'
    # generate data
    dataA_raw = ''.join([str(e) for e in np.random.randint(0, 2, 1000).tolist()])
    dataB_raw = '01010110100100010010011101000101001101001101001010' \
                '10001100100001010101001010010100101000100101010101' \
                '00101001110110101100101100010101101000101001001010' \
                '11101001111010011111101101111101011101010110101010' \
                '10011011101111011101001111010101111010101011110101' \
                '10001001011101001001001110010100010100110101001001' \
                '01010010010010010010111101001001010100010101111011' \
                '01000101011101010010101000010111010001010011110100' \
                '11011010100100010011110100010100101001110100110011' \
                '00110010101010101111101010001001000010101010101010' \
                                                                     \
                '11001001000100111100100100010110010010010010010001' \
                '01000101001010001001001110010100101001010100101010' \
                '10111001110111001011111011110011001101101101011100' \
                '11111010100100100001100101010010100101010010101001' \
                '11011000101010010100101101101110101010100100100100' \
                '01000100000010110101010100010100101001001100100101' \
                '10010100010111001101010110001010101001010100100100' \
                '10100101010101001010011101010101001001010010000110' \
                '01001010100101001010010101001010010000101111101001' \
                '01010101101001001000101000010101001010010101110100'

    dataA = FlipCoinData(dataA_raw * 40)
    dataB = FlipCoinData(dataB_raw * 40)
    # display data
    display_g1(dataA, dataB)
    display_g3(dataA, dataB)

    # This figures use 1000 samples, which is not quite statistically significant.
