#!python3
import argparse

from tokenizer.tokenizer import Tokenizer


def parse_args():
    parser = argparse.ArgumentParser(description='Zlang transpiler to C')

    parser.add_argument('source',
                        default='main.zl',
                        type=str,
                        help='source file path')
    parser.add_argument('-o',
                        '--output',
                        dest='output',
                        default=None,
                        type=str,
                        help='output files dir')

    return parser.parse_args()


def main(source='main.zl', output='.'):
    with open(source, 'r') as input:
        while True:
            tokenizer = Tokenizer(input)
            print(tokenizer.next_token())


if __name__ == '__main__':
    main(**parse_args().__dict__)
