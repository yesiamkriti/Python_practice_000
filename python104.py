#regex 3:30 24/12/22
import re
# value = "this is a string"
# output = re.search("^This.**string$",value)
# print(output)
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])(?=.*{8,})"
print(pattern)