# encapsulation -- write a data in one place close to eacher othwer is known as encapulation
# abstraction -- to reduce or hide complexcity
# some special naming convention
# name mangling
class Phone:
    def __init__(self, brand,model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}...")
    def full_name(self):
        return f"{self.brand} {self.mnodel_name}"
    def send_message(self):
        pass #twilio

phone1 = Phone('nokia', '1100',1000)
print(phone1.price)
l = [1,2,3,4]
print(l.sort())
# _name /_hero ---these type of variable for conventio of private property name
# __nem__  --- this is dunder/magic methods

