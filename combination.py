#
# An example of combinations
#

from itertools import combinations

chars = ['a','b','c','d']
print "Possible Duplets"
for comb in combinations(chars, 2):
    print comb
