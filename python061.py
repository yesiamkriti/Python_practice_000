n = str(input())
p=0
while p< len(n):
    print(f"{n[p]} :{n.count(n[p])}")
    p+=1