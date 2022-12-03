# how to remove unwanted space 
name = "     kr      iti    "
dot = "............."
print(name + dot)
print(name.lstrip() + dot)
print(name.rstrip() + dot)
print(name.strip() + dot)
print(name.replace(" ","") + dot)