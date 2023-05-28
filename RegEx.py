#RegEx Program

import re

string = """Integer : 4, 188, 213041
Float : 1.0
Double : 15.3
Float Ending in f : 11.5f
Capital letters followed by lower case followed by digits:
CAsd858
Exactly 3 digits, followed by at least 2 letters:
933RWB 619la 073a"""

# Floats are to be defined as numbers with a decimal point and a scale of 1.
# For example 2.3 is considered a float, but 2.31 is not

pattern1 = '\d+'
ints = re.findall(pattern1, string)

pattern2 = '\d+[.]\d'
floats = re.findall(pattern2, string)

pattern3 = '\d+[.]\d+'
doubles = re.findall(pattern3, string)

pattern4 = '\d+[.]\d+[f]'
floatf = re.findall(pattern4, string)

pattern5 = '[A-Z]+[a-z]+[0-9]+'
cld = re.findall(pattern5, string)

pattern6 = '[0-9]{3,}[a-z]{2,}|[0-9]{3,}[A-Z]{2,}'
d2L = re.findall(pattern6, string)

print("Integers:",ints)
print("Floats:",floats)
print("Doubles:",doubles)
print("Floatf:",floatf)
print("Capital, Lower:",cld)
print("3 digits, at least 2 letters:",d2L)
