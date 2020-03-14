import re

src = """September 1 9:13:14 arch audit[123]: SERVICE_STOP pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=systemd-hostnamed comm="systemd" exe="/usr/lib/systemd/systemd" hostname=? addr=? terminal=? res=success'"""

pattern = r"\w+\s\d{1,2}?\s(\d{1,2}?:?){3}\s\w+\saudit\[\d+\]:\s"

# Задача: разобрать строку на логические поля: временная отметка, хост, сервис, PID, сообщение
# Концепция: именованные группы
# Нужно разобрать части регулярного выражения на эти самые логические поля

# Пробел - разделяет группы в нашей ситуации
# pattern = r"(?P<time>\w+\s\d{1,2}?\s(\d{1,2}?:?){3})\s(?P<hostname>\w+)\s(?P<service>audit)\[(?P<pid>\d+)\]:\s(?P<message>.*)$"
pattern = r"^(?P<time>\w+\s\d{1,2}?\s\d{1,2}?:\d{1,2}?:\d{1,2}?)\s(?P<hostname>\w+)\s(?P<service>audit)\[(?P<pid>\d+)\]:\s(?P<message>.*)$"


# Теперь мы можем вызывать по группам
result = re.match(pattern, src)
# print(result.group('time'))
# print(result.group('hostname'))
# print(result.group('service'))
# print(result.group('pid'))
# print(result.group('message'))

journal = []  # Лист словарей, мы хотим синтаксис типа 
# Для этого нужен особый метод в библиотеке re

# Скорее всего, внутри search, поэтому в pattern допишем ^ для поиска от начала строки journal[0]['time']
find = re.finditer(pattern, src)
for s in find:
    print(s.groupdict())
    journal.append(s.groupdict())

# Теперь журнал в Linux представлен в виде объектов в нашей прогамме, на которые мы хотим явно ссылаться
print(journal[0]['time'])


# Красивая запись регулярного выражения
pattern = r"""
^(?P<time>\w+  \s  \d{1,2}?  \s  \d{1,2}?:\d{1,2}?:\d{1,2}?)  \s  # месяц день время
(?P<hostname>\w+)\s
(?P<service>[\w-]+)      # Любые буквенные символы, знак _ и знак -
\[  (?P<pid>\d+)  \]:\s  # формат [123]
(?P<message>.*)$
"""
