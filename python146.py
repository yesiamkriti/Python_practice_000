class Laptop:
    discount_precent =10 # class variable /class attribute
    babua = 0
    def __init__(self,brand,brand_name,price):
        Laptop.babua += 1
        self.brand = brand
        self.name = brand_name
        self.price = price
        self.laptop_name = brand + " " + brand_name
    @classmethod
    def count_instance(cls):
        return f"you have craeted {cls.count_instance} of person class"
    @classmethod
    def from_string(cls, string):
        first,second,third = string.split(",")
        return cls(first, second, third)



    def apply_discount(self):
        off_price = (Laptop.discount_precent/100)*self.price # if we have to change class variable for specific object then we will write self 
        return self.price - off_price
# Laptop.discount_percent =100
laptop1 = Laptop('hp','au114txx',1255465)
laptop2 = Laptop('dell','del114txx',2255465)

laptop2.discount_percent=50
print(laptop2.apply_discount())
print(laptop2.__dict__) #property
print(Laptop.babua)
print(Laptop.count_instance())
print(laptop.from_string("hello,muiugvv,kljuhu"))
