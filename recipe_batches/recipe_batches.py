#!/usr/bin/python

import math

def recipe_batches(dict_of_recipe, dict_of_ingredients):
#find all the keys of the recipe
#place them in a new array
  recipe_keys = [key for key in dict_of_recipe.keys()]
  print(recipe_keys)

#check if they exist in the ingredients
  ingredients_keys = [key for key in dict_of_ingredients.keys()]
  print(ingredients_keys)

  whole_recipe_amount_filter = []

  for key in recipe_keys:
    if key in ingredients_keys:
      continue
#if not, return 0
    else:
      return int("0")

#if true,
#loop through every key
  for key in recipe_keys:
# capture amount per key  in recipe
# capture amount per key  in ingredient
    recipe_value = dict_of_recipe[key]
    ingredient_value = dict_of_ingredients[key]
# divide the recipe amount by the ingredient amount (HAD BACKWARDS!!!!)
# floor the result
    possibly_whole_recipe_amount = ingredient_value // recipe_value
    print(possibly_whole_recipe_amount)
# append the result to an amount of whole recipes array
    whole_recipe_amount_filter.append(possibly_whole_recipe_amount)
# if the index of the key value we are on equals the length of the key array UNNECESSARY STEP
# process the results array with sort
    whole_recipe_amount_filter.sort()
  print(whole_recipe_amount_filter)
# capture the first value of that array
  amount_of_recipes_possible = whole_recipe_amount_filter[0]
# return that value
  return amount_of_recipes_possible





if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))