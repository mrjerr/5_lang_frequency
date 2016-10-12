#!/usr/bin/env python3
import re
import argparse
from os.path import exists
from collections import Counter


def load_data(filepath: str) -> list:
    with open(filepath, encoding='UTF-8') as f:
        return f.read()

def get_most_frequent_words(text: str, number: int) -> list:
    "return most frequent words [(word1, freq1),..(wordN, freqN)]"
    words = re.findall(r'\w+', text.lower())
    return Counter(words).most_common(number)

def parse_args():
    "Setup argparse"
    parser = argparse.ArgumentParser(
        description='Count most frequent words from text file')
    parser.add_argument('-file', dest='filepath', help='path to file')
    parser.add_argument('-n', dest='number',
        help='number of words to print, default value is 10')
    return parser.parse_args()

def main():
    args = parse_args()
    number = 10 if not args.number else int(args.number)
    if not args.filepath or not exists(args.filepath):
        print('\nNo such file or directory, check path\nusage: \
            {} [-h] [-file FILEPATH] [-n NUMBER]\n'.format(__file__))
        return
    text = load_data(args.filepath)
    most_frequent_words = get_most_frequent_words(text, number)
    print('{} most_frequent_words:'.format(number))
    for w, fr in most_frequent_words:
        print('{:>25}: {}'.format(w, fr))

if __name__ == '__main__':
    main()
