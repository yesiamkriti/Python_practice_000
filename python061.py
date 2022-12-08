n = str(input())
temp_var =""
p=0
while p< len(n):
    if n[p] not in temp_var:
        temp_var += n[p]
        print(f"{n[p]} :{n.count(n[p])}")
    p+=1