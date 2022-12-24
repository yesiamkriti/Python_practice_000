f1 =open("img3.jpg","rb")
# print(f1.read())
f2 = open("img3_copy.jpg","wb")
for i in f1:
    f2.write(i)
import os
if os.path.exists("img3_copy.jpg"):
    os.remove("img3_copy.jpg")
else:
    print("file does exit")