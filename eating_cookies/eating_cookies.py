#!/usr/bin/python

import sys
import math

# Fibonacci with cache

# cache = {0: 1, 1: 1}
# def rec_fib(n):
#     # base cases
#     # if n == 0:
#     #     return 1
#     # if n == 1:
#     #     return 1
#     if n in cache:
#         return cache[n]
# ​
#     # if it's not in the cache, we must 
#     n_minus_1 = rec_fib(n-1)
#     n_minus_2 = rec_fib(n-2)
#     cache[n] = n_minus_1 + n_minus_2
# ​
#     return cache[n]
# ​
# ​
# print(rec_fib(999))
# ​
# print(rec_fib(1000))


# helper function to get the value of the factorial of that number

def factorial(n):
    if n <= 1:
        return 1
    else:
        step_down_value = n - 1
        print(step_down_value)
        amount = n * factorial(step_down_value)
        print(amount)
    return amount

def evaluate_input(n, cache):
    cache = {}
    if n <=0:
      return 1
    elif n== 1:
      return 1
    elif n == 2:
      return 2
    elif n ==3:
      return 4
    elif n in cache:
      return cache[n]
    else:
      cache[n] = evaluate_input(n - 1, cache) + evaluate_input(n-2, cache) + evaluate_input(n-3, cache)
    return cache[n]


    #PROPER WHITEBOARDING --- See what work is being repeated, see the pattern
#     Eating cookies whiteboard:
# n = 1
# 1. 1 cookie 1 time
# n = 2
# 1. 1 cookie 1 time 1 cookie 1 time
# 2. 2 cookie 1 time
# n = 3
# 1. 1 cookie 1 time 1 cookie 1 time 1 cookie 1 time
# 2. 2 cookie 1 time 1 cookie 1 time
# 3. 1 cookie 1 time 2 cookie 1 time
# 4. 3 cookie 1 time
# n = 4
# 1. 1 cookie 1 time 1 cookie 1 time 1 cookie 1 time 1 cookie
# 2. 2 cookie 1 time 1 cookie 1 time 1 cookie
# 3. 1 cookie 1 time 2 cookie 1 time 1 cookie
# 4. 3 cookie 1 time 1 cookie
# 1. 1 cookie 1 time 1 cookie 1 time 2 cookie
# 2. 2 cookie 1 time 2 cookie
# 1. 1 cookie 1 time 3 cookie
# n = 5
# 1. 1 cookie 1 time 1 cookie 1 time 1 cookie 1 time 1 cookie 1 cookie
# 2. 2 cookie 1 time 1 cookie 1 time 1 cookie 1 cookie
# 3. 1 cookie 1 time 2 cookie 1 time 1 cookie 1 cookie
# 4. 3 cookie 1 time 1 cookie 1 cookie
# 1. 1 cookie 1 time 1 cookie 1 time 2 cookie 1 cookie
# 2. 2 cookie 1 time 2 cookie 1 cookie
# 1. 1 cookie 1 time 3 cookie 1 cookie
# 1. 1 cookie 1 time 1 cookie 1 time 1 cookie 1 time 2 cookie
# 2. 2 cookie 1 time 1 cookie 1 time 2 cookie
# 3. 1 cookie 1 time 2 cookie 1 time 2 cookie
# 4. 3 cookie 1 time 2 cookie
# 1. 1 cookie 1 time 1 cookie 1 time 3 cookie
# 2. 2 cookie 1 time 3 cookie

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):

  amount = evaluate_input(n, cache)

  return amount


#-------------------------------------------------------------------
  #   if n <= 1:
  #   return 1
  # elif n < 3:
  #   return 2
  # else:
  #   # capture the floored: input // 3 
  # # capture the remainder input % 3
  #   num_of_3_groupings = n // 3
  #   print(num_of_3_groupings)
  #   num_remaining_cookies = n % 3
  #   #print(num_remaining_cookies)

  # # capture the num_of_3_groupings multiplied by 4
  # # capture the remainder if 2 (2 additional ways to eat these), if 1 (only 1 way to eat this)
  #   majority_groupings = num_of_3_groupings * 4
  #   if num_remaining_cookies == 2:
  #     minority_cookies = 2
  #   else:
  #     minority_cookies = num_remaining_cookies
  # # add the multiplied remainder and multiplied num_of_3_groupings together
  #   to_be_permutated = num_of_3_groupings # majority_groupings + minority_cookies
  
  # amount= factorial(to_be_permutated)
  #-----------------------------------------------------------

# for every 3 cookies in the number of cookies, there are 4 possible ways the cookie monster can eat them
# find how many groups of 3 there are in the input
# if there are a pair of cookies remaining there are 2 different ways the monster can eat them
# if there is one cookie left there is only one way the monster can eat them

# we have a factorial, then, of the input/3 multiplied by 4 plus the remainder multiplied by either 1 (if 1) or 2 (if 2)

# capture the floored: input // 3 
# capture the remainder input % 3

# capture the num_of_3_groupings multiplied by 4
# capture the remainder if 2 multiplied by 2, if 1 multiplied by 1
# add the multiplied remainder and multiplied num_of_3_groupings together

#---------------------------------------------------------------------------

#RETRY

# for number
#   1 can fill all positions, meaning always add 1 possibility
#   2 can fill the math.ceil(number/2)
#   3 can fill the math.ceil(number/3)
#   if the remainder of the number minus 3 is 2, add 2 possibilities
#   if the remainder of the number minus 2 is 2, add 2 possibilities
#   if the remainder of the number minus 3 or 2 is 1, add 0 possibilities?

# this works for 3
# not for 5, 1 3 2 2
#-------------------------------------------------------------------------------


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')