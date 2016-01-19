#!/usr/bin/env python3

import sys
from parser import parse_file

def main():
    args = sys.argv
    assert len(args) == 2
    parse_file(args[1])

if __name__ == '__main__':
    main()


