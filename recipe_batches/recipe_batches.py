#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  ## to get key -- key in recipe
  ## to get value -- value in recipe.values
  ingredients_left = []
  for key, key in zip(recipe, ingredients):
      if len(recipe) > len(ingredients):
          return 0
      else:
          ingredients_left.append(ingredients[key] - recipe[key])
          print(ingredients_left)
          for i in ingredients_left:
              if i == 0:
                  print('we are out')
                  
                  break
              else:
                    print('we are good')
          
          
    
  



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))