print(0)
print(1)
count = 2

def fib(prev1, prev2):
    global count
    if count <= 19:
        newprev = prev1 + prev2
        print(newprev)
        count += 1
        fib(prev2, newprev)
    else:
        return 
    
fib(0, 1)