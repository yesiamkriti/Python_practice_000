# string indexing
# language = "python"
# print(language[0])
# #slicing / selecting sub sequence
# #syntax - [start argument : stop argument -1:step]
# #let start argument =Sa and stop argumet =So
# print(language[::2]) # if sa and so are blank then it will considered whole letter as a word
# print(language[::-1]) # it will reverse the letters of a word
# print(language[-1::-1])# same as above
#Ask the user name and print back user name in reverse order.
#note :- try to write your programme 2 lines using string formatting
User_Name = input("Enter your name: ")
print(f"{User_Name[::-1]}")
