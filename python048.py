#take two comma seperated input from user 
#1) user's name  , example - "Harshit"
# 2) a sinle character , "h"
# output - 2 print lines 
# 1) user's name length 
# 2) count the character that inputed (bonous : case insensitive count')
name, char =input("enter user's name and character: ").split(",")# don't use space after comma here
print(f"length of your name is {len(name)}")
print(f"character count: {name.strip().lower().count(char.strip().lower())}")
