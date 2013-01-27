#
# Using Python's inbuilt module to count freq of characters
#

from collections import Counter

input = raw_input("Enter a sentence/word: ")
print Counter(input)
