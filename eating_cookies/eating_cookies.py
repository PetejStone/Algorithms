#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n == 0:
    return n
  cache = []
  count = 0
  for d in range(1, n):
    result = d + (d+1)
    print(result)
    
  # i = 0
  # for i in range(len(cache)):
  #   print('cache')
  #   print(cache[i] + cache[i])
    
    
eating_cookies(5)
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')