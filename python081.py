# min and max function
def geratest_diff(l):
    return max(l)-min(l)
num = list(map(int,input("list:").split(",")))
print(geratest_diff(num))