import re
from tabulate import tabulate


def main(args):
    path = vars(args)['path']
    windows_audit(path)


def windows_audit(path: str):
    parameter = ['Без аудита', 'Успех и сбой', 'Успех', 'Сбой']
    master_map = {}

    with open(path, 'r') as filez:

        current_table = ''
        for s in filez:
            if "Категория или подкатегория" in s:
                break
        
        for s in filez:
            if s[0] != ' ':
                current_table = s.replace('\n', '')
                master_map[current_table] = {}        
            else:
                for p in parameter:
                    if re.search(p + '$', s):
                        value = p
                        key = s.split(p)[0].strip()
                        master_map[current_table][key] = value

    for k in master_map:
        print(k)
        print(tabulate(master_map[k].items(), headers=['Параметр', 'Значение'], tablefmt="grid"))
        print()



