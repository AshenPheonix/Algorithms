#!/usr/bin/python

import sys
from itertools import combinations

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n<=1:
    return 1
  elif (cache != None and cache <= 1):
    return 1
  else:
    if cache==None:
      cache=n
    
    return (len(list( combinations(range(n),cache) ) ) + eating_cookies(n,cache-1))
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')