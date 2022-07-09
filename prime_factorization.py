#PE5

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
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

def factorization(aP, N, f):
    if N == 1:
        return True
    if N in aP:
        f.append(N)
        factorization(aP, 1, f)
        return True
    else:
        q = N
        for i in range(len(aP)):
            if q%aP[i] == 0:
                f.append(aP[i])
                q = q//aP[i]
                if q > 1:
                    factorization(aP, q, f)
                    return True
                else:
                    return True

    return True
    

N = int(input())

a = {}
f = []
aP = eratosthenes (a, N)
ret = factorization(aP, N, f)
print(f)
