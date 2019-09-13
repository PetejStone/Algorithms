#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  print('hello')
  
  ## to get key -- key in recipe
  ## to get value -- value in recipe.values
  ingredients_left = ingredients.values()
  temp_arr = []
  total_batches = []
  batches = 0


 
  def calc(recipe, ingredients_left, temp_arr, batches, done = False ):
      done = False
      if len(recipe.values()) > len(ingredients_left):
        return 0
      else:
        for key, i in zip(recipe, ingredients_left):
          print('INGREDIENT KEY')
          subtract = i - recipe[key]
          
          if subtract > 0:
              temp_arr.append(i - recipe[key])
              ingredients_left = temp_arr
              batches += 1
              

              
          else:
              print('I AM DONE')
              temp_arr.append(i - recipe[key])
              ingredients_left = temp_arr
              #batches += 1

              done = True
              #
            
             
        
       
      
      temp_arr = []
      
      print('TEMP ARRAY NOW')
      print(ingredients_left)
      print(batches)
      print(done)
      #batches += 1
      if done == True:
          print('true')
          print('BATCHES')
          length = len(ingredients_left)
          print(length)
          batches = batches//length
          if batches == 0:
             return 1
          elif len(ingredients_left) == 1:
             batches += 1
             return batches

          else:
             return batches
              
      else:
          print('false')
          print(ingredients_left)
          
          #batches += 1
          return calc(recipe, ingredients_left, temp_arr,batches) 
    
  
  
  return calc(recipe, ingredients_left, temp_arr,batches)
  
          
                  
                 
      

     # print(ingredients_left - recipe_arr)
      
      # if len(recipe) > len(ingredients):
      #     return 0
      # else:
      
      #     subtract = ingredients[key] - recipe[key]
      #     if subtract != 0:
      #         # ingredients_left.append(subtract)
      #         # print(ingredients_left)
      #         pass
      #     elif subtract == 0:
      #          print('WE ARE DONE')
      #          done == True
      #          print(ingredients_left)
            
      # for r, i in zip(recipe.values(), ingredients_left): 
      #     print(len(recipe))
      #     if len(recipe) > len(ingredients_left):
      #         print('we are out')
      #         print(batches)
          
      #         break
      #     else:   
            
      #         subtract = i - r
      #         if subtract != 0: 
      #             ingredients_left.append(subtract)
      #         print(ingredients_left)  
      #         print('we are good')
      #         batches += 1
          
            
          
  
                  
          
          
    
  



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))