# Операции над файлами

# Задача: заменить все слова "audit" на "journal" и последнюю строку на "END"
with open("audit-short.txt", "r") as src:  # Открыть на чтение
    with open("audit-copy.txt", "w") as dst:  # Открыть на запись
        for s in src:
            new = s.replace("audit", "journal")  # Новая строка, которую впишем в результат
            dst.write(new)

# Мы не можем определить конец файла до того, как его прочитаем. Такой подход к редактированию файлов неудобен
# Решение через буферизацию

buf = []  # Буфер для файла
with open("audit-short.txt", "r") as src:
    for s in src:
        # append - добавить элемент в конец массива
        buf.append(s)  # Заполняем буфер всем файлом (так нельзя поступать для гигантских файлов)

with open("audit-copy.txt", "w") as dst:
    for b in buf[:-1]:  # От начала до последней строки, не вкоючая ее
        dst.write(b.replace("audit", "journal"))
    dst.write("END")

# Более понятный синтаксис для отрезания последней строки
# Результат тот же самый
buf.pop()  # pop - выдать последний элемент массива, удалив его из массива
with open("audit-copy.txt", "w") as dst:
    for b in buf:
        dst.write(b.replace("audit", "journal"))
    dst.write("END")


