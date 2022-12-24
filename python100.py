# # unit 5 date - 24/12/2022 last chapter
# f = open('demo.txt','r')
# print(f.read())
# print(f.readline(1))
# print(f.writable())
# g = open("demo.txt", 'w')
# print(g.write("i am writing this text from pythoni am writing this text from pythoni am writing this text from pythoni am writing this text from pythoni am writing this text from pythoni am writing this text from pythoni am writing this text from pythoni am writing this text from pythoni am writing this text from pythoni am writing this text from pythoni am writing this text from pythoni am writing this text from pythoni am writing this text from pythoni am writing this text from pythoni am writing this text from python"))
# for i in f :
#     g.write(i)
# try:
#     f = open('demo.txt')
#     #your code goes here
# finally:
#     f.close()
# # This why we are making sure that file is closed properly even if raised that cause the program flow to stop
# with open ("demo.txt")as f:
#     f.read()# --->example
#     #your code goes here
f = open("demo.txt","r")
print(f.read(6))
print(f.tell())
print(f.seek(target))
