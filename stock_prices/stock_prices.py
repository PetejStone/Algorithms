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
    cur_max = 1 #start at the zero index
    cur_min = 0
    new_arr = []
    for i in range(1, len(prices)):
        if prices[i] > prices[cur_max ]:
            cur_max = i
            
            new_arr = prices[ 1: 4]
       
            
       
        # if len(new_arr) == 0:
        #     new_arr = prices
            
            
        # else:
        #     new_arr = new_arr
        # for j in range(len(new_arr)):
        #     if prices[j] < prices[cur_min]:
        #         cur_min = j
        #         print(prices[cur_min])
    print(f'LENGTH {new_arr}')
    print(f'CURRENT MAX {prices[cur_max]}')
    print(f'CURRENT_MIN {prices[cur_min]}' )
   # subtract = prices[cur_max] - prices[cur_min]
    #print(f'SUBTRACT {subtract}')
    #return subtract
    
    

       # print(prices[i]
  
                    
        # SWAP 
        ###swap example
        #####         > <
        ## swap [ 1,2,4,3,5 ]
        ## inside loop found that 4 is > 3, so new cur_index is 3 (3)
        ### temp = arr[2] (4) - the current position, so temp value is 4
        #### arr[2] == arr[3] -- so 4 is now = 3 -> [1,2,3,3,5]
        ###### arr[cur_index] (arr[3]) == 4 -> [1,2,3,4,5]

        ####
        # temp = arr[i] #temp variable is == the current position in the outside loop
    
        # arr[i] = arr[cur_index] #current position of outside loop is set equal to the new current index from the inside loop
       
        # arr[cur_index] = temp #current index is set equal to the temp variable

    # for i in range(len(prices)):
    #   if prices[i] > prices[i + 1]:
    #     current_max = prices[i]
    #   else:
    #     current_max = prices[i + 1]
    #   print(f'current_max: {current_max}')
    #   new_arr = prices[ : i]
    #   print(f"prices: {new_arr}")
    #   for j in range(len(new_arr)):
    #     if prices[j] < prices[j + 1]:
    #       current_min = prices[j]
    #     else:
    #       current_min = prices[j + 1]
    #     print(f'current min {current_min}')
    #     #print(prices(j))

          
   
    

    
 
 
  


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))