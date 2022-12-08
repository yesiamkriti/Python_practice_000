# range (start argument , stop argument , step argument)
# stop argument carry n-1 term if we write n.
#  steps means how many steps to jump i.e  to left 
# eg if we put(1,11,1) then output will be 
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# here it will jump 0 steps
# but if we put (0,10,3)then output will be
# 1
# 4
# 7
# it will jump 2 steps
for i in range(1,11,1):
    print(i)
for x in range(1,10,3):
    print(x)
for y in range(10,0,-1):
    print(y)
for z in range(1,-11,-1):
    print(z)