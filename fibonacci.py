def fib(n):
    stack=[]
    a=0
    b=1
    for i in range(2,n):
        stack.append(a)
        stack.append(b)
        a=a+b
        b=a+b
    return stack

fib(7)
