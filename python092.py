# exercise 
# define a function that takes a number (n)
# return a dictionary containing cube of numbers from 1 to not

# example
# cube_finder(3)
# {1:1, 2:8,3:27}


def cube_finder(n):
    dict1={}
    for x in range(1,n+1):
        dict1[x] = x**3
    return(dict1)
print(cube_finder(10))

