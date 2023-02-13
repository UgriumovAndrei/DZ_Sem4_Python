# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
#  находясь перед некоторым кустом заданной во входном файле грядки.
# 4
# 1 2 3 4
# 9
n = int(input('Введите количество кустов: '))
g = []
for i in range(n):
    g.append(int(input('Введите количество ягод на кусте: ')))
if n<=3:
    print(sum(g))
else:
    maxsum = -1
    for i in range (n):
        sum = 0
        if i != n-1:
            sum += g[i]+g[i-1]+g[i+1]
        else:
            sum = g[i-1]+g[i]+g[0]
        if sum>maxsum:
            maxsum = sum
    print(maxsum)
    
    
        
