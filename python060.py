# exercise -watch coco
# ask user's name and age 
# if user's name start with ('a' or 'A') and age is above 10 then
# print you can watch coco movie
# else print sorry tou cannot watch coco
Name,Age =str(input("your name and age:")).split(",")
if Name[0]=="a" or Name[0]== "A" and age>=10:
    print("YOU CAN WATCH COCO MOVIE")
else:
    print("SORRY YOU CANNOT WATCH COCO MOVIE")