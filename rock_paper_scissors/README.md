# Rock Paper Scissors

Write a function `rock_paper_scissors` to generate all of the possible plays that can be made in a game of "Rock Paper Scissors", given some input `n`, which represents the number of plays per round. 

For example, given n = 2, your function should output the following:

```python
[['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]
```

Your output should be a list of lists containing strings. Each inner list should have length equal to the input n.

n number of plays
list of possible plays:
[['rock'], ['paper'], ['scissors']]

at 1 play:
[['rock'], ['paper'], ['scissors']]

at 2 plays:
[
    ['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'],    
    ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'],
    ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]

at 3 plays:
[
    ['rock', 'rock', 'rock'], ['rock', 'paper', 'rock'], ['rock', 'scissors', 'rock'],
    ['rock', 'rock', 'paper'], ['rock', 'paper', 'paper'], ['rock', 'scissors', 'paper'],
    ['rock', 'rock', 'scissors'], ['rock', 'paper', 'scissors'], ['rock', 'scissors', 'scissors'],

    ['paper', 'rock', 'rock'], ['paper', 'paper', 'rock'], ['paper', 'scissors', 'rock'],
    ['paper', 'rock', 'paper'], ['paper', 'paper', 'paper'], ['paper', 'scissors', 'paper'],
    ['paper', 'rock', 'scissors'], ['paper', 'paper', 'scissors'], ['paper', 'scissors', 'scissors'],

    ['scissors', 'rock', 'rock'], ['scissors', 'paper', 'rock'], ['scissors', 'scissors', 'rock']
    ['scissors', 'rock', 'paper'], ['scissors', 'paper', 'paper'], ['scissors', 'scissors', 'paper']
    ['scissors', 'rock', 'scissors'], ['scissors', 'paper', 'scissors'], ['scissors', 'scissors', 'scissors']
    
    ]

the pattern for the outer list is the last amount of them (n-1) multiplied by 3 
    for each list in list(n-1):
        addedRock = []
        addedRock.append([list.copy() + ['rock']])

        addedPaper = []
        addedPaper.append([list.copy() + ['paper']])

        addedScissors = []
        addedScissors.append(list.copy() + ['scissors'])

        list = addedRock + addedPaper + addedScissors
    return list
    we need the previous list before we can finish the for

    and our base case is list[1]:
        return [['rock'], ['paper'], ['scissors']]
    also, list[0]:
        return [[]]
the pattern for the inner list is n



if n == 0:
    return [[]]
else:
    addLists(n)


def addLists(plays):
    if plays == 1:
        return [['rock'], ['paper'], ['scissors']]
    else:
        previousList = addLists(plays - 1)
        for outcomeList in previousList:
            addedRock = []
            addedRock.append([outcomeList.copy() + ['rock']])

            addedPaper = []
            addedPaper.append([outcomeList.copy() + ['paper']])

            addedScissors = []
            addedScissors.append(outcomeList.copy() + ['scissors'])

            outcomeList = addedRock + addedPaper + addedScissors
    return outcomeList

## Testing

Run the test file by executing `python test_rps.py`.

You can also test your implementation manually by executing `python rps.py [n]`.

## Hints

 * You'll want to define a list with all of the possible Rock Paper Scissors plays.
 * Another problem that asks you to generate a bunch of permutations, so we're probably going to want to opt for using recursion again. Since we're building up a list of results, we'll have to pass the list we're constructing around to multiple recursive calls so that each recursive call can add to the overall result. However, the tests only give our function `n` as input. To get around this, we could define an inner recursive helper function that will perform the recursion for us, while allowing us to preserve the outer function's function signature. 
 * In Python, you can concatenate two lists with the `+` operator. However, you'll want to make sure that both operands are lists!
 * If you opt to define an inner recursive helper function, don't forget to make an initial call to the recursive helper function to kick off the recursion.