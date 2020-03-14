# ЗадачаЖ Вывести строки, которые содержат сообщение от сервиса audit

with open("audit-short.txt") as src:
    for s in src:
        if "audit" in s:  # Наличие элемента в массиве
            print(s, end="")

print()

# В данном случае ловятся левые сообщения, не только от сервиса audit. Примитивное регулярное выражение работает плохо
with open("audit.txt") as src:
    for s in src:
        if "audit" in s:  # Наличие элемента в массиве
            print(s, end="")