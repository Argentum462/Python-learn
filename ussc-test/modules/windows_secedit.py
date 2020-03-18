import re
from tabulate import tabulate


def main(args):
    path = vars(args)['path']
    verbose = vars(args)['verbose']
    max_width = vars(args)['max_width']
    windows_secedit(path, verbose, int(max_width))


def windows_secedit(path: str, is_verbose: bool, max_width: int):
    master_map = {}
    reduction_map = {}

    pattern = r"\[(?P<table>[\w\s]+)\]"


    with open(path, 'r') as filez:
        current_table = ''
        for s in filez:
            if re.match(pattern, s):
                current_table = re.match(pattern, s).group('table')  
                master_map[current_table] = {} 
                reduction_map[current_table] = {} 
            else:
                key = s.split('=')[0].strip()
                value = s.split('=')[1]
                if len(value) > max_width:
                    reduction_map[current_table][key] = value
                    master_map[current_table][key] = value[:max_width]+"..."
                else:
                    master_map[current_table][key] = value
        

    for k in master_map:
        print(k)
        print(tabulate(master_map[k].items(), headers=['Параметр', 'Значение'], tablefmt="grid"))
        print()
        if is_verbose == True:
            for h in reduction_map[k]:
                print(h, reduction_map[k][h], sep=' = ')

    if is_verbose == False:
        for k in reduction_map:
            if len(reduction_map[k]) > 0:
                print('Слишком длинные поля таблиц были сокращены. Для отображения сокращенных строк используйте -v или задайте большую максимальную длину -m ЧИСЛО')
                break
        

