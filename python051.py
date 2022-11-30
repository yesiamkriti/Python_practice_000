# use of  center and put star
name = "kriti"
print(name.center(len(name),"*"))
print(name.center(len(name)+2,"*"))
print(name.center(len(name)+4,"*"))
print(name.center(len(name)+10,"*"))
#string are immutable
string= "string"
#we can't change string 
print(string.replace("t", "T"))# it does not mean that actual string is change 
# string[0]="t"
# print(string) # these will not work because strings are immutable
