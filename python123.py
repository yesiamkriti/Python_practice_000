l = [(1,2),(4,3),(5,6),(7,8)]
print(list(zip(*l)))
l1, l2 = list(zip(*l))
print(list(l1),list(l2))
# print the max number from l3 and l2 by comparing the same index number
# eg 4> 2 print 4 ....and so on ...[4, 8, 7, 2, 3]
l2 = [4,5,3,1,2]
l3 = [2,8,7,2,3]
l4 = []
for pair in zip(l2,l3):
    l4.append(max(pair))
print(l4)