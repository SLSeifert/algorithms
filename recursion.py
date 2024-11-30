#Call stack example
def fact(x):
    print(x)
    if x == 1:
        return 1
    else:
        return x * fact(x-1)
    
print(fact(3))

#Fibonacci sequence using recursion
def Fibonacci(inx):
    if inx <= 1:
        return inx
    else:
        return Fibonacci(inx-1)+Fibonacci(inx-2) 

print(Fibonacci(2))

#Fibonacci using iterative function
def fibonacci(inx):
    seq = [0,1]
    for i in range(inx):
        seq.append(seq[-1]+seq[-2])
    return seq[-2]

print(fibonacci(8))