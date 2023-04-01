import random
ms = [random.randint(-50, 50) for i in range(random.randint(10, 20))]
print(*ms)
max = int(input(" максимума = "))
min = int(input("минимум = "))
mas = []
if max >= min:
    for i in range(len(ms)):
        if max >= ms[i] and min <= ms[i]:
            mas.append(i)
    print("количество:", len(mas))
    print("индекс:", mas)
