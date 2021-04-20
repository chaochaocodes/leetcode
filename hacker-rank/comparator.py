'''
Sorting: Comparator

Comparators are used to compare two objects. In this challenge, you'll create a comparator and use it to sort an array. The Player class is provided in the editor below. It has two fields:

1. name: a string.
2. score: an integer.

Sort first descending by score, then ascending by name if players have the same score. 

To do this, you must create a Checker class that implements the Comparator interface, then write an int compare(Player a, Player b) method implementing the Comparator.compare(T o1, T o2) method. In short, when sorting in ascending order, a comparator function returns -1 if a < b, 0 if a = b, and 1 if a > b.
'''

# intput

# amy 100
# david 100
# heraldo 50
# aakansha 75
# aleksa 150

# output:
# aleksa 150
# amy 100
# david 100
# aakansha 75
# heraldo 50

from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        pass
    
    def comparator(a, b):
        if a.score < b.score:
            return 1
        if a.score > b.score:
            return -1
        if a.name < b.name:
            return -1
        if a.name > b.name:
            return 1
        return 0
