from __future__ import print_function
import sys
import argparse
from nltk import tokenize

class Preprocess:
    def __init__(self):
        self.task = 'preprocess'

    def proc(self):
        while 1:
            try: line = sys.stdin.readline()
            except KeyboardInterrupt: break
            if not line: break
            line = line.strip()
            if not line: continue
            if '</doc>' == line:
                print('')
                continue
            if '<doc' == line[:4]: continue
            if '[[' == line[:2]: continue
            lines = tokenize.sent_tokenize(line)
            for l in lines:
                print(l)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    pre = Preprocess()
    pre.proc()
