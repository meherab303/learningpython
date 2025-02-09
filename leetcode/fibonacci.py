def fib(n):
    # f_n={}
    # f_n[0]=0
    # f_n[1]=1
    # for i in range(2,n+1,1):
    #     f_n[i]=f_n[i-1]+f_n[i-2]
    # return f_n[n] 
    if n <= 1:
        return n  # Base case: f(0) = 0, f(1) = 1
    return fib(n - 1) + fib(n - 2)   

print(fib(8))