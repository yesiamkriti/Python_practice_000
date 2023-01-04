# advance min() and max()
names = ['Kavya Singh','kriti','harshit','a']
print(max(names,key = lambda item:len(item)))


student1 = [
    {'name':'kavya singh', 'score':90, 'age':17},
    {'name':"kriti",'score':92,'age':19},
]
print(max(student1,key =lambda item :item.get('age'))['name'])


student2 = {
    'Harshit':{'score':50, 'age':11},
    'mohit':{'score':43, 'age':12},
    'sunita':{'score':46, 'age':11.5}
}
print(max(student2,key = lambda item : student2[item]['score']))