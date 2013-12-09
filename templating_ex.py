#
# Simple example to illustrate String templating
#

import string

values = {'name': 'Kiran', 'age': 24, 'grade': 9.0}

templ = string.Template("""
Name: $name
Age: $age
Grade: $grade
""")

student = templ.substitute(values)

print 'TEMPLATE: ', student
