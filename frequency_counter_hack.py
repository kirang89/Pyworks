#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from collections import Counter

#
# A clever data structure to use as a frequency counter
#

frequency = defaultdict(Counter)

# Defining some sample data
frequency['fruits']['mango'] = 9
frequency['fruits']['orange'] = 4
frequency['fruits']['banana'] = 2

# Incrementing mangoes
frequency['fruits']['mango'] += 1

# Print frequency of each fruit
print dict(frequency['fruits'])

# Get the fruit that is highest in quantity
print frequency['fruits'].most_common(1)