#regex 3:30 24/12/22
import re
# value = "this is a string"
# output = re.search("^This.**string$",value)
# print(output)
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])(?=.*{8,})"
# this is known as regex....
# r is a literal raw
# ^ ---- this is known as circumflex . it is used to start a string in regex from
# ()--- this is used to define a type of container 
# ? --- question mark is use for zero and one occurance
# . ----- dot is use for any character (except newline character)
# * ----- is use for zero and one occurence
# []------ sqare bracket is used as container or set

# -    this is used to define range
# updated