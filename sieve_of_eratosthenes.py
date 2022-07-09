#Sieve of Eratosthenes
primes = {}

N = int(input())
for i in range(2, N+1):
    primes[i] = True
    
print(primes)

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
        print(i, primes[i])
