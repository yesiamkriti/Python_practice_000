class Laptop:
    def __init__(self):
        print("start")
    def config(self):
        print("hp","i5","1tb")

laptop1 = Laptop()
laptop2 = Laptop()
# Laptop.config(laptop1)
laptop1.config()
laptop2.config()