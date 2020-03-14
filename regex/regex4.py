import re

pattern = r"""
^
(?P<time>\w+  \s  \d{1,2}?  \s  \d{1,2}?:\d{1,2}?:\d{1,2}?)  \s  # месяц день время
(?P<hostname>\w+)\s
(?P<service>[\w-]+)         # Любые буквенные символы, знак _ и знак -
(\[  (?P<pid>\d+)  \]:\s)?  # формат [123], у kernel PID вообще нет, поэтому в вопросике
(?P<message>.*)
$
"""

journal = []

with open("journal.txt", "r") as filez:
    for line in filez:
        find = re.finditer(pattern, line, re.VERBOSE)
        for f in find:
            journal.append(f.groupdict())

for entry in journal:
    if entry["service"] == "kernel":
        print(entry)

    