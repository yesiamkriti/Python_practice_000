#26-11-2022 3 pm to 5 pm
tuple1 = ("A","B","C","D","E")
(one,*two,three) = tuple1
print(one)
print(two)
print(three)
# write a program to unpack the following tuple into four variables and print each variables
# tuple1 = (10,20,30,40)
tuple2 = (10,20,30,40)
(a,b,c,d) = tuple2
print(a)
print(b)
print(c)
print(d)
#tupel3 = (10,20)
#tupel4 = (30,40)
# swap above tuples
#output - tuple3 = (30,40)
#tupel4 = (10,20)
tupel3 = (10,20)
tupel4 = (30,40)
tupel5 = tupel4
print(tupel5)
tupel5=tupel3
print(tupel5)
my_tupel = ("car", "bus","train")
for x in my_tupel:
    print(x)
i=0
while i<len(my_tupel):
    print(my_tupel[i])
    i+=1
    #list insid tupel6
tupel6 = (1,[6,7],2,3,4,5,)
a = tupel6[1][0]
print(a)
tupel6[1][0]=8
print(tupel6)


