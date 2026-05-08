prev1 = 0
prev2 = 1

print(prev1)
print(prev2)

for i in range(18):
    newPrev = prev1 + prev2
    print(newPrev)
    prev1 = prev2
    prev2 = newPrev
