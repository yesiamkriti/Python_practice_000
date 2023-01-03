# this is challange
# [1,2,3] , [4,5,6], [7,8,9]
# return average
# (1+2+7)/3 , (2,5,8)/3 , (3,6,9)/3
# try to make this anonymous function in one line using lambda

# def average_finder(*arg):
#     average = []
#     for pair in zip(*arg):
#         average.append(sum(pair)/len(pair))
#     return average
p=(lambda *arg:[sum(pair)/len(pair)for pair in zip(*arg)])
print(p([1,2,3], [4,5,6], [7,8,9]))

