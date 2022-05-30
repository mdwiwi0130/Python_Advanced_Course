def divide_0 (func):
    def inner(n,d):
        if(d==0):
            return 0
        else:
            return func(n,d)
    return inner

@divide_0
def divide(n, d):
       return n / d

n = int(input("請輸入分子"))
d = int(input("請輸入分母"))
print(divide(n,d))
