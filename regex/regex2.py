import re

src = """September 1 9:13:14 arch audit[123]: SERVICE_STOP pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=systemd-hostnamed comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
fsdjdhdihd
Mar 14 18:15:22 arch kernel: audit: type=1130 audit(1584191722.393:102): pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=NetworkManager-dispatcher comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
shf 45 dhdj jdddg
Mar 1 19:00:22 arch audit[324]: SERVICE_START pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=NetworkManager-dispatcher comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
dshdsf 456 sdfjwhr
Mar 14 18:15:32 dimas audit[1]: SERVICE_STOP pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=NetworkManager-dispatcher comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
Mar 14 18:15:32 arch kernel: audit: type=1131 audit(1584191732.360:103): pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=NetworkManager-dispatcher comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'
"""
# Mar 14 
pattern = r"\w+\s\d{1,3}?"
# for s in src.split('\n'):  # Сделали массив строк из одной огромной, разбив по символу переноса строки
#     if re.search(pattern, s):
#         print(s)

# Строка "dshdsf 456 sdfjwhr" попала в паттерн, хотя мы просили от 1 до 2 цифр. Она действительно подходит 

# Нужно добавить разделитель прямо в паттерн
pattern = r"\w+\s\d{1,2}?\s"
# for s in src.split('\n'):
#     if re.search(pattern, s):
#         print(s)

# Теперь добавим время
pattern = r"\w+\s\d{1,2}?\s\d{1,2}?:\d{1,2}?:\d{1,2}?"


# Избавимся от повторов
pattern = r"\w+\s\d{1,2}?\s(\d{1,2}?:?){3}"
# for s in src.split('\n'):
#     if re.match(pattern, s):  # match - искать только с начала строки
#         print(s)

# Учтем имя хоста после времени

pattern = r"\w+\s\d{1,2}?\s(\d{1,2}?:?){3}\s\w+"


# Наконец, находим нужный сервис
pattern = r"\w+\s\d{1,2}?\s(\d{1,2}?:?){3}\s\w+\saudit"

# Уточним, что там есть квадратная скобка (их экранируем)
# Мы ищем вот такой паттерн Mar 1 19:00:22 arch audit[324]:
pattern = r"\w+\s\d{1,2}?\s(\d{1,2}?:?){3}\s\w+\saudit\[\d+\]:\s"


for s in src.split('\n'):
    if re.match(pattern, s):  
        print(s)
