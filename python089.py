#in keyword and iterations in dictionary
user_info = {
    'name' : 'Kriti',
    'age' : 19,
    'fav_movies' : ['coco','kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],
}

# check if key exist in dictionary
if 'name' in user_info:
    print('present')
else:
    print('not present')

# check if values exist in dictionary
if ['coco','kimi no na wa'] in user_info.values():
    print('yes kriti is a value of key name')
else:
    print('no, this is not a value of any keys ')

#loops in dicitionary
for i in user_info.keys():
    print(i)
for j in user_info.values():
    print(j)

# values method
user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))

# keys method
user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

# way to print key or value in loop form
# that is loops in dictionaries
for i in user_info.values():
    print(i)
# or 

for i in user_info:
    print(user_info[i])

# for loops of keys in dictionary
for i in user_info:
    print(i)

#item method
user_items = user_info.items()
print(user_items)
print(type(user_items))
#output of item will in the form [('k1','v1'),('k2','v2'),('k3','v3')]

#or
for key,value in user_info.items():
    print(f'key is {key} and value is {value}')
# or dictionary touple unpacking
for i in user_info.items():
    print(i)