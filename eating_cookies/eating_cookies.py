#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    if n == 1 or n == 0: 
        return 1
    elif n == 2: 
        return 2
    n1 = 1
    n2 = 1
    n3 = 0

    for i in range(n - 1):
        # Bottom up approach, counting up to result
        result = n3 + n2 + n1 # === eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1) 
        n3 = n2
        n2 = n1
        n1 = result
    return result
 

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')