# add and delete data
user_info = {
    'name' : 'Kriti',
    'age' : 19,
    'fav_movies' : ['coco','kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],
}
# to add data
user_info['fav song'] = ['song1','song2']
print(user_info)

#pop method
user_info.pop('age') # in pop parenthesis we have to write a key otherwise it show error
print(user_info)

#or to know popped item 
popped_item = user_info.pop('fav_tunes')
print(f'popped item is {popped_item}')
print(user_info)

#popitem method :  it used when we have to delete a last keys' value .it will give answer in *****tuple form
popped_item1 = user_info.popitem()
print(f'popped item 1 is : {popped_item1}')
print(type(popped_item1))

#update method
more_info = {'name':'Abhijeet','state':'bihar'}
user_info.update(more_info)
print(user_info)