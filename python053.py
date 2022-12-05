#dictonary
mydictionary = {
    "name":"Nikhil",
    "age":22,
    "age": 23 , #over write when dublicate is add
    "percent": 89
}
print(mydictionary.get("age"))
print(mydictionary.values())
print(mydictionary.keys())
print(mydictionary)
print(mydictionary.items())
mydictionary["roll number"] = 8
print(mydictionary)
mydictionary.update({"age" :33})
print(mydictionary)
mydictionary.pop("age")
print(mydictionary)
mydictionary.popitem()
print(mydictionary)
#ordered
#changeable
#does not allow dubilcate value