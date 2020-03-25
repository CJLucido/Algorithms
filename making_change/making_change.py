#!/usr/bin/python

import sys
import math


def dime_growth_rate(n):
  if n <= 10:
    return 1
  if n <= 20:
    return 4
  else:
    dime_possibilities = (((n-10)//10) * 2) + dime_growth_rate(n-10) + 1
    print(dime_possibilities)
  return dime_possibilities

def quarter_growth_rate(n):
  if n <= 25:
    return 1
  if n <= 50:
    return 12
  else:
    quarter_possibilities = ((n//25)* 11) + quarter_growth_rate(n-25) + 1
  print(quarter_possibilities)
  return quarter_possibilities

def making_change(n, denominations, cache=None):
  cache = {}

  if n <= 0: 
    return 1
  elif n < 5 and 1 in denominations: 
    penny_possibilities = 1
    return 1
  elif n == 5 and 5 in denominations:
    penny_possibilities = 1
    nickel_possibilities = 1
    return 2
  elif n == 10 and 10 in denominations:
    penny_possibilities = 1
    nickel_possibilities = 2
    dime_possibilities = 1
    return 4
  elif n == 25 and 25 in denominations:
    penny_possibilities = 1
    nickel_possibilities = 6
    dime_possibilities = 6
    quarter_possibilities = 1
    return 14
  elif n == 50 and 50 in denominations:
    penny_possibilities = 1
    nickel_possibilities = 10
    dime_possibilities = 24
    quarter_possibilities = quarter_growth_rate(n) #12
    half_dollar_possibilities= 1
    return 48
  elif n > 50 and n % 5 == 0 and n%10 == 0:
    penny_possibilities = 1
    nickel_possibilities = n//5 #(this is correct)
    dime_possibilities = dime_growth_rate(n) #THIS IS INACCURATE
    quarter_possibilities = quarter_growth_rate(n)
    half_dollar_possibilities= math.ceil(n/50)
    return (1 + nickel_possibilities + dime_possibilities + quarter_possibilities + half_dollar_possibilities)
  elif n > 20 and n < 50 and n % 5 == 0 and n%10 == 0:
    penny_possibilities = 1
    nickel_possibilities = n//5 #(this is correct)
    dime_possibilities = dime_growth_rate(n) #THIS IS INACCURATE
    quarter_possibilities = 2
    print(dime_possibilities)
    # half_dollar_possibilities= 
    return (1 + nickel_possibilities + dime_possibilities + quarter_possibilities)
  elif n % 5 == 0 and n%10 == 0:
    penny_possibilities = 1
    nickel_possibilities = n//5 #(this is correct)
    dime_possibilities = dime_growth_rate(n) #THIS IS INACCURATE can't forget the plus one for actually landing on the value (we aren't just increasing the amount of steps up)

    quarter_possibilities = quarter_growth_rate(n)
    # half_dollar_possibilities= 
    return (1 + nickel_possibilities + dime_possibilities)
  elif n % 5 == 0 and n%10 != 0:
    penny_possibilities = 1
    nickel_possibilities = (n//5) + 1 #(this is correct)
    dime_possibilities = dime_growth_rate(n) #THIS IS INACCURATE unsure for these inbetween numbers
    quarter_possibilities = quarter_growth_rate(n)
    # half_dollar_possibilities= 
    return (1 + nickel_possibilities + dime_possibilities)
  elif n in cache:
    return cache[n]
  else:
    cache[n] = making_change(n - 1,denominations, cache)  #making_change(n-2,denominations, cache) + making_change(n-3,denominations, cache)
    return cache[n]

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")