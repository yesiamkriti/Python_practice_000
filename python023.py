a=int(input("starting prime no.:"))
b=int(input("ending prime no.:"))
if a > 1:
    for i in range(a,b):
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
           print(i)          
