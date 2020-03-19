#!/usr/bin/python

import sys

def addLists(plays):
    if plays == 1:
        return [['rock'], ['paper'], ['scissors']]
    else:
        previousList = addLists(plays - 1)
        newList = []
        for outcomeList in previousList:
            addedRock = outcomeList.copy() + ['rock']
            
            addedPaper = outcomeList.copy() + ['paper']

            addedScissors = outcomeList.copy() + ['scissors']

            newList.append(addedRock)
            newList.append(addedPaper)
            newList.append(addedScissors)
           
    return newList

def rock_paper_scissors(n):
  if n == 0:
      return [[]]
  else:
      outcomes = addLists(n)
  return outcomes




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')