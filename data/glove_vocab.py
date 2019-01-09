from __future__ import print_function
import sys
import argparse

class Tok:
    def __init__(self):
        self.task = 'tok'

    def proc(self):
        while 1:
            try: line = sys.stdin.readline()
            except KeyboardInterrupt: break
            if not line: break
            line = line.strip()
            tokens = line.split()
            word = tokens[0]
            print(word)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    args = parser.parse_args()

    tok = Tok()
    tok.proc()
