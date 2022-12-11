# define a function which will take list containing numbers as input 
# and return list containing square of every elements

# example 
# numbers = [1,2,3,4]
# square_list(numbers) ----->return ----> [1,4,9,16]
def square_list(l):
    square = []
    for x in l:
        square.append(x**2)
    return square
numbers = list(range(1,20))
print(square_list(numbers))