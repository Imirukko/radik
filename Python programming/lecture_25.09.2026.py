
#task_1
temperature_C = int(input("Введите температуру в градусах Цельсия: "))
temperature_F = (temperature_C * 9/5) + 32
temperature_K = temperature_C + 273.15

print("Температура в Фаренгейтах: ", temperature_F)
print("Температура в Кельвинах: ", temperature_K)


#task_2
n = int(input("Введите число: "))

if n % 2 == 0:
    print(n, "- четное число")
else:
    print(n, "- нечетное число")
if n > 0:
    print(n, "- положительное число")
elif n < 0:
    print(n, "- отрицательное число")
else:
    print(n, "- ноль")
if 10 <= n <= 50:
    print(n, " находится в диапазоне от 10 до 50")


#task_3
import random
import string

password_list = (
    random.choices(string.ascii_uppercase, k=3) +
    random.choices(string.digits, k=3) +
    random.choices('!@#$%^&*', k=2)
)
random.shuffle(password_list)
password = ''.join(password_list)
print(password)



#task_4
import collections

sentence = input("Введите предложение: ").lower().replace(" ", "")
result = collections.Counter(sentence).most_common(3)
print("Три наиболее часто встречающиеся буквы:", result)



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
