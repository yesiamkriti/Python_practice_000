
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
def hello():
    print("hello world")
    hello()
hello()
