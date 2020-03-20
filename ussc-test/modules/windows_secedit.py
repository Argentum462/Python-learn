import re
from tabulate import tabulate
import modules.translations as translations


def main(args):
    path = vars(args)['path']
    verbose = vars(args)['verbose']
    max_width = vars(args)['max_width']
    translate = vars(args)['translate']
    windows_secedit(path, verbose, int(max_width), translate)


def windows_secedit(path: str, is_verbose: bool, max_width: int, is_translate: bool):
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
                if is_translate == False:    
                    key = translate(key)
                value = s.split('=')[1]
                if len(value) > max_width:
                    reduction_map[current_table][key] = value
                    master_map[current_table][key] = value[:max_width]+"..."
                else:
                    master_map[current_table][key] = value
        

    for k in master_map:
        if is_translate == False:
            print(translate(k))
        else:
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
        

def translate(string: str) -> str:
    if string in translations.get().keys():
        return translations.get()[string]
    return string