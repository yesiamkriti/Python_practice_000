#dataHiding 24/12/2022
class person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
person1 = person("kriti",19)
print(person1._person__name)