# fromkeys
dict1 = {"name":"kriti" , "age":19}
dict1 = dict.fromkeys(['name','age','state'], 'unknown')
print(dict1)
dict1 = dict.fromkeys(['name','age','state'], ['unknown','unknown'])
print(dict1)
# dict1 = dict.fromkeys(range(0,11), 'unknown')
# print(dict1)

# get method
print(dict1['name']) #----1
# or
print(dict1.get('name')) #-----2
# output of both case is same if name is present in dict1 but if name is not in dict1 then case1 show error but case2 show None
#we can change the value None e.g print(dict1.get('fav' , 'not found!'))

# use of get method
if 'name' in dict1:
    print("present")
else:
    print('absent')
#or 
if dict1.get('name'): # if None ----> False, else -----> True
    print('present')
else:
    print('absent')
# copy
dict2 = dict1.copy()
print(dict2)
#clear
dict1.clear()
print(dict1)