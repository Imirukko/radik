#task_5
def f(N):
    list1 = [True] * (N + 1)
    list1[0] = list1[1] = False
    for i in range(2, int(N**0.5) + 1):
        if list1[i]:
            for j in range(i*i, N + 1, i):
                list1[j] = False
    primes = [x for x in range(N + 1) if list1[x]]
    return primes
print(f(1337))
