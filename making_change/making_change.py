#!/usr/bin/python

import sys

def making_change(n, denominations):
  penny_possibilities = 0
  nickel_possibilities = 0
  dime_possibilities = 0
  quarter_possibilities = 0
  half_dollar_possibilities = 0

  if n == 0:
    return 1
  elif n % 50 == 0 and 50 in denominations:
    penny_possibilities = 1 
    half_dollar_possibilities = n//50
    quarter_possibilities = n//25
    dime_possibilities = n//10 
    nickel_possibilities = n//5
  elif n % 25 == 0 and 25 in denominations:
    penny_possibilities = 1 
    quarter_possibilities = n//25
    dime_possibilities = n//10 
    nickel_possibilities = (n//5) + 1 
  elif n > 25 and n % 10 == 0 and 10 in denominations:
    penny_possibilities = 1
    quarter_possibilities = n//25 * n//10 - 1
    dime_possibilities = n//10 * n//10
    nickel_possibilities = n//5
  elif n % 10 == 0 and 10 in denominations:
    penny_possibilities = 1
    dime_possibilities = n//10 * n//10
    nickel_possibilities = n//5
  elif n > 5 and n % 5 == 0 and 5 in denominations:
    penny_possibilities = 1
    nickel_possibilities = (n//5) + 1 
  elif n == 5 and 5 in denominations:
    penny_possibilities = 1
    nickel_possibilities = (n//5) 
  elif n < 5 and 1 in denominations:
    penny_possibilities = 1
  print(  penny_possibilities, +\
  nickel_possibilities, +\
  dime_possibilities, +\
  quarter_possibilities, +\
  half_dollar_possibilities)
  total_possibilities = penny_possibilities + nickel_possibilities + dime_possibilities + quarter_possibilities + half_dollar_possibilities 
  return total_possibilities

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")