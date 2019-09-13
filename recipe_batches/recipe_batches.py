#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  print('hello')
  
  ## to get key -- key in recipe
  ## to get value -- value in recipe.values

  ## temp variables
  ingredients_left = ingredients.values() # ingredients left set to the values of ingredients 
  temp_arr = [] #temp arr set to empth
  batches = 0  #batches set to 0


 
  def calc(recipe, ingredients_left, temp_arr, batches, done = False ):
      done = False # done set to false for recursion
      if len(recipe.values()) > len(ingredients_left): #if the length of the recipe list is > than length of ingredients, you do not have that ingredient so return 0
        return 0
      else:
        for key, i in zip(recipe, ingredients_left): # zip puts lists side by side in order and automatically discards extra items if one is longer
          print('INGREDIENT KEY')
          subtract = i - recipe[key] # subtract = ingredient value - recipe value
          
          if subtract > 0: # if the subtracted value is greater than 0, you still have ingredients left
              temp_arr.append(i - recipe[key]) ## append whats left into temp array
              ingredients_left = temp_arr # set ingredients left to the new values of whats left
              batches += 1 # add one to batches (this is adding once PER INGREDIENTS) -> Will divide below to get correct #
              

              
          else: # if ingredients reach 0 or below
              print('I AM DONE') 
              temp_arr.append(i - recipe[key]) #still append to whats left
              ingredients_left = temp_arr # set new whats left to new array -- needed for dividing by grabbing length of array
              #batches += 1

              done = True # set done to true to stop recursion
              #
            
             
        
       
      
      temp_arr = [] #after each round, reset temp array to empty so it's not appending the same list
      
      print('TEMP ARRAY NOW')
      print(ingredients_left)
      print(batches)
      print(done)
      #batches += 1
      if done == True: # if done and no ingredients left
          print('true')
          print('BATCHES')
          length = len(ingredients_left) # get length of items in ingredients_left --

          ##    Need to divide the number of batches (one was added per item), and divide that by the items
          ##    in the list to actually get the equivelant of ONE batch
          batches = batches//length ## divide  --> //  <-- floors the divided #
          if batches == 0: #if batches == 0, that means it was rounded down from a floating point # < 1, which means at last ONE batch was made
             return 1 # return the one batch
          elif len(ingredients_left) == 1: #if the length of the ingredients left == 0, it means you used ALL items exactly, so you can't divide and are one batch short
             batches += 1 # add that one batch
             return batches #return total batches

          else:
             return batches #if none conditions above, return total batches
              
      else: ## if state is still false and ingredients are left
          print('false')
          print(ingredients_left)
          
          #batches += 1
          return calc(recipe, ingredients_left, temp_arr,batches) # re run the calc funtion using recursion
    
  
  
  return calc(recipe, ingredients_left, temp_arr,batches) # return the value from the recursion calc function which will == total recipes
  
          
                  
                 
      

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