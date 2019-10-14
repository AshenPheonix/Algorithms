#!/usr/bin/python

import sys
from itertools import product

def rock_paper_scissors(n):
  
  return [ list(item) for item in list(product(['rock','paper','scissors'],repeat=n)) ]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')