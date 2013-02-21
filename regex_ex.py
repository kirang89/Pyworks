#!/usr/bin/env python
#
# Common Regex's
#
import re

#Email regex
str = 'abc@gmail.com,blah,monkey boy, dude@yahoo.com, something'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)
print emails

#Searching for a pattern in a string
str = "an example word:dog"
match = re.search(r'word:\w\w\w', str)
if match:
    print 'Pattern', match.group(), 'found'
else:
    print 'Pattern not found'

#Another example for pattern search
langs = ['Python', 'Ruby', 'PHP', 'Java', 'C++']
pattern = '^C|^J|^R'

for lang in langs:
    if re.search(pattern, lang, re.IGNORECASE):
        print lang, "found"
    else:
        print lang, "not found"

#Substituting values using regex
str = 'Python is an average language'
print "Before replace, string: ", str
mod_text = re.sub('average', 'awesome', str)
print "After replace, string: ", mod_text

#Compiling patterns for reuse
#Only alphabets allowed
checker = re.compile(r"[^A-Za-zs.]")
str1 = "HelloWorld"
str2 = "4elloa7as98da890d"
if checker.search(str1):
    print "str1 does not satisfy"
else:
    print "str1 done"
if checker.search(str2):
    print "str2 does not satisfy"
else:
    print "str2 done"

#Checking phone numbers
checker = re.compile(r"[^0-9s.]")
str1 = "Hello World"
str2 = "123981723"
if checker.search(str1):
    print "str1 invalid"
else:
    print "str1 valid"
if checker.search(str2):
    print "str2 invalid"
else:
    print "str2 valid"

#Find email domain in a string
str = "My name is Kiran and my kiran.daredevil@gmail.com is my email address"
res = re.search(r"@[\w.]+", str)
if res.group:
    full_path = res.group()
    domain = full_path.split('@')[1]
    print "domain server:", domain
