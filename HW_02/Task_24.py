"""
В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких 
собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с 
двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед 
некоторым кустом заданной во входном файле грядки.
Пример:
4 -> 1 2 3 4
9
"""
n = int(input("Введите количество кустов на грядке: "))
berries = list(map(int, input().split()))

adjacent_berries = [0] * n
for i in range(n):
    if i == 0:
      adjacent_berries[i] = berries[i] + berries[n - 1]
    elif i == n - 1:
      adjacent_berries[i] = berries[i] + berries[0]
    else:
      adjacent_berries[i] = berries[i] + berries[i - 1] + berries[i + 1]
      max_berries = max(adjacent_berries)
print(max_berries)      
