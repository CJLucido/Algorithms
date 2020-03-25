# Recipe Batches

Write a function that receives a recipe in the form of a dictionary, as well as all of the ingredients you have available to you, also in the form of a dictionary. Both of these dictionaries will have the same form, and might look something like this:

```python
{
  'eggs': 5,
  'butter': 10,
  'sugar': 8,
  'flour': 15
}
```

def show_whole_batches(dict_of_recipe, dict_of_ingredients):

The keys will be the ingredient names, with their associated values being the amounts. In the case of the recipe dictionary, these amounts will represent the amount of each ingredient needed for the recipe, while in the case of the ingredients dictionary, the amounts represent the amounts available to you.

dict_of_recipe = {
'eggs': 5,
'butter': 10,
'sugar': 8,
'flour': 15

}

dict_of_ingredients = {
'eggs': 5,
'butter': 10,
'sugar': 8,
'flour': 15

}

#find all the keys of the recipe
#place them in a new array
#check if they exist in the ingredients
#if not, return 0
#if true,
#loop through every key
capture amount in recipe
capture amount in ingredient
divide the recipe amount by the ingredient amount
floor the result
append the result to an amount of whole recipes array
if the index of the key value we are on equals the length of the key array
process the results array with sort
capture the first value of that array
return that value

Your function should output the maximum number of whole batches that can be made for the supplied recipe using the ingredients available to you, as indicated by the second dictionary.

For example

```python
# should return 0 since we don't have enough butter!
recipe_batches(
  { 'milk': 100, 'butter': 50, 'flour': 5 },
  { 'milk': 138, 'butter': 48, 'flour': 51 }
)
```

## Testing

Run the test file by executing `python test_recipe_batches.py`.

You can also test your implementation manually by executing `python recipe_batches.py`.

## Hints

- If there's a dictionary operation you aren't sure of how to perform in Python, look it up!
- What's the _minimum_ number of loops we need to perform in order to write a working implementation?
