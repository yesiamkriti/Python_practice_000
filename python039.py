'''sets
store multiple values in single variable
1)unordered
2)dublicates are not allowed '''
myset = {"car","bike","boat"}
print(myset)
print(len(myset))
if "bike" in myset:
    print(True)
else:
    print(False)
myset.remove("boat")
print(myset)