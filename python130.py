# advance sorted () function
fruits = ['garpes','apple','mango']
fruits.sort()
print(fruits)
fruits2 = ('kiwi','garpes','apple','mango')
print(sorted(fruits2))
guitars = [
    {'model':'yahama f310', 'price':8400},
    {'model':'faith naptune','price':8600},
    {'model':'faith apollo','price':8500}
    ]
sorted_gitars = sorted(guitars,key = lambda d : d['price'],reverse = True)
print(sorted_gitars)