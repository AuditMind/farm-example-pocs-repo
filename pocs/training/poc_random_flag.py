#!/usr/bin/env python3
import sys

from helpers import generate_flag


def main():
    if len(sys.argv) != 2:
        print('usage: poc_random_flag.py <target>', file=sys.stderr, flush=True)
        return 2

    print('training target={}'.format(sys.argv[1]), file=sys.stderr, flush=True)
    print(generate_flag(), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
