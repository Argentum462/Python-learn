print('Hello')  # Python - интерпретируемый язык программирования

"""
Это
многострочный
комментарий
Интерпретируемый значит, что не нужна компиляция
"""

print('H' * 10)
print(True)

if "a" == True:
    print("a is true")
else:
    print("not true")

if "" == False:
    print("Empty")

if "":
    print("Empty")

if "non-empty":
    print("non-empty")

# Все, что не ноль - True

if 0 == False:
    print("Zero false")

if 25:
    print("Not false")

# Как нормально проверять строчки

if len("non-empty") != 0:
    print("Непустая строчка с норм проверкой")

if len("") == 0:
    print("Пустая строчка")
