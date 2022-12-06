def div(a,b):
    print(a/b)
def good_div(func):
    def inner_div(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner_div

div=good_div(div)
div(2,4)