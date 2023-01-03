def my_sum(*arg):
    if all([(type(i)==int or type(i)==float) for i in arg]):
        total=0
        for num in arg:
            total += num
        return total
    else:
        return "wrong input"
print(my_sum(1,2,3,45,6,4,7,5.45))