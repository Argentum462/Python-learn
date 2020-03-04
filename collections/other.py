list = [1, 2, 2, 3, 3, 3]
print(list)

st = set(list)  # set([1, 2, 2, 3, 3, 3]) - не содержит повторов
print(st)

dic = {
    0: "Zero",
    1: "One",
    2: "Two"
}
print(dic)
print(dic[0])
print()

dic = {
    "Denis": {"sex": "female", "city": "Moscow", "age": 202},  # это значение позже затирается
    "Denis": {"sex": "male", "city": "Moscow", "age": 20},  # этим, так как ключи одинаковые
    "Lena": {"sex": "female", "city": "Sochi", "age": 30}  
}
print(dic)
print(dic["Denis"]["sex"])

# создание строки вручную, требует str(...), когда складываем строку с не-строкой
print(str(dic["Denis"]["age"]) + " years old and " + dic["Denis"]["city"] + " and ..")

# вставить вычисления прямо в строку, не требует выполнения str(...) на не-строках: все, что в {...} - автоматически строка
print(f'Denis is {dic["Denis"]["age"]} years old and {dic["Denis"]["city"]} and random function {213 + 5 * 7}')

for k in dic:
    print(f'{k}:{dic[k]}')

# вставить в словарь новое значение
dic["Sasha"] = {"sex": "female", "city": "London", "age": 40}
print(f'Sasha {dic["Sasha"]}')


