#!/usr/bin/python

import argparse

def find_max_profit(prices):
 ## current_min_price_so_far and the max_profit_so_far
 ## take in an array of prices (numbers)
 ## go through array and find biggest number
 ## set biggest number as stopping point
 ## go through array second time up to the biggest number and find the SMALLEST number
 ## subtract the smallest number from the biggest number
     # loop through n-1 elements
    cur_max = 1 #start at the one index -- start one index because the first element CANT be the biggest
    cur_min = 0  #set current min to zero index because once that max is found, the array stops -- so the current min may be larger than the cur max
    new_arr = [] # set black array for when splitting
    for i in range(1, len(prices)): # start at the first index because we don't want to consider the first element
        if prices[i] > prices[cur_max ]: # if the item is greater than the current max,
            cur_max = i #set current max to that index -- this will keep changing until it reaches the highest # in the array
             
            new_arr = prices[ : cur_max] #split everything AFTER the current max is found
       

        for j in range(len(new_arr)): # new variable for finding min
            if prices[j] < prices[cur_min]: #if a number is found that is less than the first index
                cur_min = j #set that to the new min
                print(prices[cur_min])
    print(f'NEW ARRAY {new_arr}') # new split array
    print(f'CURRENT MAX {prices[cur_max]}') #current max value
    print(f'CURRENT_MIN {prices[cur_min]}' ) #current min value
    subtract = prices[cur_max] - prices[cur_min] #subtract the curent max from the min
    #print(f'SUBTRACT {subtract}')
    return subtract #return subtracted value
     
  

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))