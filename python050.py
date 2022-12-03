# use of replace and find
string="she is beautiful and she is good girl"
print(string.replace("is","was",2))#2 represent how many is will convert into was
print(string.find("is", 2))# 2 represent from where to start find is
x= string.find("is")
print(string.find("is",x+1))# here x+1 because if we put x it will analyse 1 st is only
