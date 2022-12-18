# chracter count in dictionary
def char_count(word):
    count={}
    for x in word :
        count[x]= word.count(x)
    return (count)
print(char_count("Abhijeet"))