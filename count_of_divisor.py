# 約数の数
maxctr = 0
for i in range(1, 2001):
    ctr = 0
    for j in range(1,i):
        if i%j == 0:
            ctr += 1
    maxctr = max(ctr, maxctr)
    if maxctr == ctr:
        print(i, maxctr)
    #print(ctr, i)
print(maxctr)
