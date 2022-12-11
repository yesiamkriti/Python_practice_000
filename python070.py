# define is_palindrome function that atake one word in string as input 
# and return True if it ie palindrome else return False


# palindrome - word that reads same backwards as forwards


# example
# is_palindrome("madam") -------True
# is_palindrome("naman") -------True
# is_palindrome("horse") -------False


# logic(alogrithm)
# step1 -> reverse the string
# step2 -> cmpare reversed string with original string
def palindrome(word):
    return (word[0:] == word[::-1])
word = input("Enter the word to know palindrome :")
print(palindrome(word))