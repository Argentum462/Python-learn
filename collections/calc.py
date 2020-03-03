import sys

# Сумма аргументов командной строки

mas = sys.argv

k = 0
b = 0
for a in mas:
    if k == 0:
        k += 1
        continue
    else:
        b = b + int(a)
print(b)        

k = 0
b = 0
c = len(mas)
while(c > 0):
    if k == 0:
        k += 1
        c -= 1
        continue
    else:
        b = b + int(mas[c])
        c -= 1
print(b)
