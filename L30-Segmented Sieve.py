import math

L, R = map(int, input().split())

r = int(math.sqrt(R)) + 1
# Determining all prime numbers upto square roor of Right Limit.

primes = []
lst = [1] * r
i = 2
while (i * i <= R):
    if lst[i]:
        primes.append(i)
        j = i * i
        while (j < r):
            lst[j] = 0
            j += i
    i += 1

# Now we will take a list in desired range(R-L+1). Then we will make 0 of all
# multiples of those prime numbers. They must are composite number. Rests are
# prime numbers in that range.
ranged_primes = [1] * (R - L + 1)
for i in range(R - L + 1):
    if ranged_primes[i]:
        for j in primes:
            if (L + i) % j == 0 and (L + i) != j:
                ranged_primes[i] = 0
                k = i
                while (k < R - L + 1):
                    ranged_primes[k] = 0
                    k += j
                break

for i in range(R-L+1):
    if ranged_primes[i]:
        print(i+L)
