filez = open("audit-short.txt", "r")  # Открыть файл в режиме чтения
# Файл можно использовать
for s in filez:
    print(s, end='')  # end позволяет не ставить \n туда, где он уже есть (например, строки из логов)
filez.close() # Закрыть файл

with open("audit-short.txt", "r") as filez:  # файл открыт только внутри этого блока
    for s in filez:
        print(s, end="")



