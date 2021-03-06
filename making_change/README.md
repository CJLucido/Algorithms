# Making Change

You work as a bank teller, handling people's bank transactions (this is your
part-time gig while you're studying at Lambda). 

One day one of the wealthiest and also most eccentric patrons of the bank walks
up to your stall. They hand you some cash and tell you they want you to figure
out exactly how many ways there are to make change for the amount of money they
plopped down in front of you using only pennies, nickels, dimes, quarters, and
half-dollars. 

pennies
nickels
dimes
quarters
half-dollars

def making_change(input_in_cents, arr_of_coin_denominations):
  calculate total ways to make change with the given coin denominations

Since this is a bank, you have an infinite supply of coinange. Write a function
`making_change` that receives as input an amount of money in cents as well as an
array of coin denominations and calculates the total number of ways in which
change can be made for the input amount using the given coin denominations. 

For example, `making_change(10)` should return 4, since there are 4 ways to make
change for 10 cents using pennies, nickels, dimes, quarters, and half-dollars:

 1. We can make change for 10 cents using 10 pennies
 2. We can use 5 pennies and a nickel
 3. We can use 2 nickels
 4. We can use a single dime

for 0:
there is 1 way to return change (no change)
for 1:
there is 1 way to return change (only a penny)
for 2:
there is 1 way to return change (only pennies)
for 3:
there is 1 way to return change (only pennies)
for 4:
there is 1 way to return change (only pennies)
for 5:
there are 2 ways to return change (pennies or a nickel)
for 6:
there is 2 ways to return change (pennies or penny and a nickel)
for 7:
there is 2 ways to return change (pennies or pennies and a nickel)
for 8:
there is 2 ways to return change (pennies or pennies and a nickel)
for 9:
there is 2 ways to return change (pennies or pennies and a nickel)
for 10:
there is 4 ways to return change (pennies, pennies and a nickel, nickels, or dime)
for 11:
there is 4 ways to return change (pennies, pennies and a nickel, 2 nickels and penny, or dime and a penny)
for 12:
there is 4 ways to return change (pennies, pennies and a nickel, 2 nickels and pennies, or dime and pennies)
for 13:
there is 4 ways to return change (pennies, pennies and a nickel, 2 nickels and pennies, or dime and pennies)
for 14:
there is 4 ways to return change (pennies, pennies and a nickel, 2 nickels and pennies, or dime and pennies)
for 15:
there is 6 ways to return change (pennies, pennies and a nickel, 2 nickels and pennies, 3 nickels, dime and pennies, or dime and nickel)
for 16:
there is 6 ways to return change (pennies, pennies and a nickel, 2 nickels and pennies, 3 nickels and pennies, dime and pennies, or dime and nickel with penny)
for 17:
there is 6 ways to return change (pennies, pennies and a nickel, 2 nickels and pennies, 3 nickels and pennies, dime and pennies, or dime and nickel and pennies)
for 18:
there is 6 ways to return change (pennies, pennies and a nickel, 2 nickels and pennies, 3 nickels and pennies, dime and pennies, or dime and nickel and pennies)
for 19:
there is 6 ways to return change (pennies, pennies and a nickel, 2 nickels and pennies, 3 nickels and pennies, dime and pennies, or dime and nickel and pennies)
for 20:
there is 9 ways to return change (pennies, pennies and a nickel, 2 nickels and pennies, 3 nickels and pennies, 4 nickels, dime and pennies, dime and nickel and pennies, dime and 2 nickels, or 2 dimes)
1 4 4

for 30:
there is 18 ways to return change (pennies, pennies and a nickel, 2 nickels and pennies, 3 nickels and pennies, 4 nickels and pennies, 5 nickels and pennies, 6 nickels, dime and pennies, dime and nickel and pennies, dime and 2 nickels and pennies, dime and 3 nickels and pennies, dime and 4 nickels, 2 dimes and pennies, 2 dimes a nickel and pennies, 2 dimes and 2 nickels, 3 dimes, quarter and pennies, quarter and a nickel)
 1 6 9 2

 for 40:
    P (penny possibilities is always 1)
    NP, 2NP, 3NP, 4NP, 5NP, 6NP, 7NP, 8N (nickel possibilities are alway n//5, unless n %10 != 0)
    DP, DNP, D2NP, D3NP, D4NP, D5NP, D6N, 2DP, 2DNP, 2D2NP, 2D3NP, 2D4N, 3DP, 3DNP, 3D2N, 4D
    QP, QNP, Q2NP, Q3N, QDP, QDN
    1 8 16 6
 

 for 50:
     penny_possibilities = 1
    nickel_possibilities = 10
    dime_possibilities = 24
    quarter_possibilities = 12, QP, QNP, Q2NP, Q3NP, Q4NP, Q5N, QDP, QDNP, QD2NP, QD3N, Q2DN, 2Q
    half_dollar_possibilities= 1

  for 75:
    QP, QNP, Q2NP, Q3NP, Q4NP, Q5NP, Q6NP, Q7NP, Q8NP, Q9NP, Q10N, QDP, QDNP, QD2NP, QD3NP, QD4NP, QD5NP, QD6NP, QD7NP, QD8N, Q2DNP,Q2D2NP,Q2D3NP,Q2D4NP,Q2D5NP,Q2D6N,Q3DNP,Q3D2NP,Q3D3NP,Q3D4N, Q4DNP, Q4D2N, Q5D, 2QP,2QNP,2Q2NP,2Q3NP,2Q4NP,2Q5N,2QDNP,2QD2NP,2QD3N,2Q2DP, 2Q2DN, 3Q
  1 16 26 

  for 100:
    1 20 37 

patterns so far:
  we always have the option of pennies
  for every increment to the 5th position we add a nickel option
  for every increment to the 10th position we add a dime option (and implicitly a nickel method)
  we can probably assume that this pattern will happen for every 25th position, we add a quarter option (and implicitly a nickel option)
  and also for every 50th position, we add a half-dollar option(and implicitly a quarter option, a dime option, and a nickel option)

so we are always building on the last pattern BUT the options are only increasing if we have gone up by 5, 10, 25, or 50

the nickel options increase in amount to the floored value of n / 5
    so anything from 15 and 20 (exclusive) will have 3 nickel methods
the dime options increase in amount to the floored value of n / 10 UNTIL hitting the next 5th position before the next tenth, at the midpoint (like 15) it adds another nickel option to the dime options
    this means if the current position is divisible by 5 without a remainder but not by 10 without a remainder:
        increase the nickel options by 1 extra
        increase the dime option to the floored value of n/10 (to the flrd value, not by the flrd value)
    else:
        just increase dime options

penny_possibilities = 0
nickel_possibilities = 0
dime_possibilities = 0
quarter_possibilities = 0
half_dollar_possibilities = 0

if n == 0:
  return 1
elif n % 50 == 0:
  increase penny possibilities to 1 
  increase half-dollar possibilities TO n // 50
  increase quarter possibilities TO n // 25
  increase dime possibilities TO n//10 
  increase nickel possibilities To n//5
elif n % 25 == 0:
  increase penny possibilities to 1 (not during recursion, would just be base case?)
  increase quarter possibilities TO n // 25
  increase dime possibilities TO n//10 (not during recursion)
  increase nickel possibilities To n//5 + 1 (by + 1, in recursion)
elif n % 10 == 0:
  increase dime possibilities TO n//10
  increase nickel possibilities TO n//5
elif n % 5 == 0:
  increase nickel possibilities To n//5 + 1 (by + 1, in recursion)
elif n < 5:
  increase penny possibilities to 1

total_possibilities = penny_possibilities + nickel_possibilities + dime_possibilities + quarter_possibilities + half_dollar_possibilities 


  penny_possibilities = 0
  nickel_possibilities = 0
  dime_possibilities = 0
  quarter_possibilities = 0
  half_dollar_possibilities = 0

  cache = {}

  if n <>= 0: (base case)
    return 1
  elif n < 5 and 1 in denominations: (base case)
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
    quarter_possibilities = 12
    half_dollar_possibilities= 1
    return 48
  elif n in cache:
      return cache[n]
  else:
      cache[n] = evaluate_input(n - 1, cache) + evaluate_input(n-2, cache) + evaluate_input(n-3, cache)
    return cache[n]

    P (penny possibilities is always 1)
    NP, 2NP, 3NP, 4NP, 5NP, 6NP, 7NP, 8NP, 9NP, 10N (nickel possibilities are alway n//5, unless n %10 != 0)
    DP, DNP, D2NP, D3NP, D4NP, D5NP, D6NP, D7NP, D8N, 2DP, 2DNP, 2D2NP, 2D3NP, 2D4NP, 2D5NP, 2D6N, 3DP, 3DNP, 3D2NP, 3D3NP, 3D4N, 4DP, 4DNP, 4D2N, 5D
    QP, QNP, Q2NP, Q3NP, Q4NP, Q5N, QDP, QDNP, QD2NP, QD3N, Q2DN, 2Q



  if n % 50 == 0 and 50 in denominations:
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
    quarter_possibilities = n//25 + # problem here, should be plus possibilities with lower denominations (too complicated for task at hand)
    dime_possibilities = n//10 * n//10
    nickel_possibilities = n//5
  elif n % 10 == 0 and 10 in denominations:
    penny_possibilities = 1
    dime_possibilities = n//10 * n//10
    nickel_possibilities = n//5
  elif n > 5 and and n/5 != 2 and n % 5 == 0 and 5 in denominations:
    nickel_possibilities = (n//5) + 1 

  
  print(  penny_possibilities, +\
  nickel_possibilities, +\
  dime_possibilities, +\
  quarter_possibilities, +\
  half_dollar_possibilities)
  total_possibilities = penny_possibilities + nickel_possibilities + dime_possibilities + quarter_possibilities + half_dollar_possibilities 
  return total_possibilities

## Testing 

For this problem, there's a test that tests your implementation with small
inputs (amounts of change up to 300 cents). There's also a separate test that
tests your implementation with large inputs (amounts of change >= 350 cents). 

You'll find that without implementing performance optimizations into your
solution, your solution will likely hang on the large input test. 

To run the tests separately, run `python test_making_change.py -k small` in
order to run just the small input test. Run `python test_making_change.py -k
large` to execute just the large input test. If you want to run both tests, just
run `python test_making_change.py`.

You can also test your implementation manually by executing `python
making_change.py [amount]`

## Hints

 * This problem can be thought of as a more difficult version of the eating
   cookies problem. 
 * As far as base cases go, again, think about some cases where we'd want the
   recursion to stop executing. What should happen when the amount of cents
   given is 0? What should happen when the amount of cents given is negative?
   What about when we've used up all of the available coin denominations?
 * As far as performance optimizations go, caching/memoization might be one
   avenue we could go down. 
 * Building up values in our cache in an iterative fashion might also be a good
   way to go about improving our implementation. 
 
   Here's a general idea: we can initialize a cache as a list (a dictionary
   would work fine as well) of 0s with a length equal to the amount we're
   looking to make change for. Each value of the list will represent the number
   of ways to make `i` cents, where `i` are the indices of the list. So
   `cache[10] == 4` from our example above. Since we know there is one way to
   make 0 cents in change, we'll initialize `cache[0] = 1` (you can seed entries
   for additional values as well, though you don't actually need to). 

   Now that we've initialized our cache, we'll start building it up. We have an
   initial value in our cache, so we'll want to build up subsequent answers in
   terms of this initial value. So, for a given coin, we can loop through all of
   the higher amounts between our coin and the amount (i.e., `for higher_amount
   in range(coin, amount + 1)`). If we take the difference between the higher
   amount and the value of our coin, we can start building up the values in our
   cache. 

   To go into a little more detail, let's walk through a small example. If we
   imagine our coin is a penny, in the first loop iteration, `higher_amount` is
   going to be 1 (since it will at first be the same value as our coin). If we
   take the difference between `higher_amount` and our coin value, we get 0. We
   already have a value for 0 in our cache; it's 1. So now we've just figured
   out 1 way to 1 cent from a penny. Add that answer to our cache. 

   Next up, on the next iteration, `higher_amount` will now be 2. The difference
   between `higher_amount` and our coin value now is 1. Well we just figured out
   an answer for 1, so now we have an answer for 2. Add that to our cache. 

   Once this loop finishes, we'll have figured out all of the ways to make
   different amounts using the current coin. At that point, all we have to do is
   perform that loop for every single coin, and then return the answer in our
   cache for the original amount!



#FIRST PASS
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
    quarter_possibilities = n//25 + # problem here, should be plus possibilities with lower denominations (too complicated for task at hand)
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


  #Second attempt ------------------------------------------------------

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
    quarter_possibilities = 12
    half_dollar_possibilities= 1
    return 48
  elif n > 50 and n % 5 == 0 and n%10 == 0:
    penny_possibilities = 1
    nickel_possibilities = n//5 #(this is correct)
    dime_possibilities = (n//10 + ((n-10)//10)) + (((n-10)/10) +((n-20)/10)) + 1 #THIS IS INACCURATE
    quarter_possibilities = math.ceil(n/25)
    half_dollar_possibilities= math.ceil(n/50)
    return (1 + nickel_possibilities + dime_possibilities + quarter_possibilities + half_dollar_possibilities)
  elif n > 20 and n < 50 and n % 5 == 0 and n%10 == 0:
    penny_possibilities = 1
    nickel_possibilities = n//5 #(this is correct)
    dime_possibilities = (n//10 + ((n-10)//10)) + (((n-10)/10) +((n-20)/10)) + 1 #THIS IS INACCURATE
    quarter_possibilities = 2
    print(dime_possibilities)
    # half_dollar_possibilities= 
    return (1 + nickel_possibilities + dime_possibilities + quarter_possibilities)
  elif n % 5 == 0 and n%10 == 0:
    penny_possibilities = 1
    nickel_possibilities = n//5 #(this is correct)
    dime_possibilities = ((n//10 + ((n-10)//10))) + 1 #THIS IS INACCURATE can't forget the plus one for actually landing on the value (we aren't just increasing the amount of steps up)

    # quarter_possibilities = 
    # half_dollar_possibilities= 
    return (1 + nickel_possibilities + dime_possibilities)
  elif n % 5 == 0 and n%10 != 0:
    penny_possibilities = 1
    nickel_possibilities = (n//5) + 1 #(this is correct)
    dime_possibilities = (n//10 + ((n-10)//10)) + (((n-10)/10) +((n-20)/10)))+ 1 #THIS IS INACCURATE unsure for these inbetween numbers
    # quarter_possibilities = 
    # half_dollar_possibilities= 
    return (1 + nickel_possibilities + dime_possibilities)
  elif n in cache:
    return cache[n]
  else:
    cache[n] = making_change(n - 1,denominations, cache)  #making_change(n-2,denominations, cache) + making_change(n-3,denominations, cache)
    return cache[n]



    -------------------------
    here is the actual equation for dime possibilities over 10
    dimes {10 : 1, 20:4, 30:9, 40:16, 50:25}
plus 2 to the last increase
the last increase starts at 1
so for every 10 higher than 10 it should be that number minus 10/10, plus 2

(20-10)/10 =1 this is the first step up from 10, then that step * 2, then that 2 plus the last increase of 1, 1 +2 =3, plus the original 1, 3+1=4, 20 
30-10/10 = 2, 2*2 = 4, 4+4=8, plus original 1, 9 at 30
40-10/10 =3, 3*2 =6, 6+9=15, plus original 1, 16 at 40
50-10/10=4, 4*2=8, 8+16=24, plus the original 1, 25 at 50


def dime_growth_rate(n):
  if n <= 20:
    return 4
  else:
    dime_possibilities = (((n-10)/10) * 2)+ dime_growth_rate(n-10)
  return dime_possibilities