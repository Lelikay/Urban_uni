numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
a = len(numbers) + 1
for i in range(1, a):
    for j in range(1, a):
        if (j == 1):
            continue
        elif i == j:
            primes.append(i)
            break
        elif i % j == 0:
            not_primes.append(i)
            break
print('Primes: ', primes)
print('Not Primes: ', not_primes)
