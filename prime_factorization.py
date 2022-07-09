def eratosthenes(primes, N):
    for i in range(2, N+1):
        primes[i] = True
        

    #sieving
    # 2 = true
    #sqrt
    for i in range(2, N+1):
        if primes[i] == True and i**2 <= N:
            for j in range(N+1):
                if i**2+i*j > N:
                    break
                primes[i**2+i*j] = False
    for i in range(2, N+1):
        if primes[i]:
            #print(i, primes[i])
            through = 0
        else:
            primes.pop(i)
    return list(primes.keys())

N = int(input())
primes = {}
aP = eratosthenes(primes, N)

f = [] #array for factorization
q = N
for p in aP:
  if q%p == 0:
    f.append(p)
    q = q//p

for i in range(2, N+1):
  
