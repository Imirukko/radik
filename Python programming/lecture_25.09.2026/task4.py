#task_4
import collections

sentence = input("Введите предложение: ").lower().replace(" ", "")
result = collections.Counter(sentence).most_common(3)
print("Три наиболее часто встречающиеся буквы:", result)
