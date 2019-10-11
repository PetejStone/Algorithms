#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n == 0:
    return [[]]
  if n == 1:
    return
  l = [['rock'], ['paper'], ['scissors']]
  
  def rps_recursive(l,n):
    i = 0
    j = 0

    initial = ['rock', 'paper', 'scissors']
    cur_list = [['rock'], ['paper'], ['scissors']]
    temp_list = [[cur_list[0][0]]]*3 + [[cur_list[1][0]]] * 3 + [[cur_list[2][0]]] * 3
    new_list = temp_list
    test_list = [['rock'], ['rock'], ['rock'], ['paper'], ['paper'], ['paper'], ['scissors'], ['scissors'], ['scissors']]
    cache = {
      0:[],  
      1: [['rock'], ['paper'], ['scissors']]
    }
    # print(cur_list[0][0])
    out_count = 0
    in_count = 0
    i = 0

    
    for i in range(len(new_list)):
      print(new_list[i])
      if new_list[i] == ['rock']:
        new_list[i] = ['rock']
        i += 1
      elif new_list[i] == ['paper']:
        new_list[i] == ['paper']
        i +=1
      elif new_list[i] == ['scissors']:
        new_list[i] = ['scissors']

   
    new_list[0].append('a')
    print(new_list)
      

    # while i < len(new_list) :
    #   new_list[i].append('.')
    #   print(new_list[i])
    #   i +=1


        
   

    

   
    
      
    # while out_count < 3:
    #   current = cur_list
    #   #new_list.append([cur_list[i], initial[a]])
    #   new_list.append(["".join(cur_list[i]), initial[a]])
    #   in_count += 1
    #   a += 1
    #   if in_count > 2:
    #     print(new_list)
    #     in_count = 0
    #     out_count += 1
    #     i += 1
    #     a = 0
        

        
  rps_recursive(l,n)
  return l
rock_paper_scissors(2)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')