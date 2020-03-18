import re
from typing import Tuple, List

def main(args):
    start = vars(args)['start']
    run = vars(args)['run']
    show = vars(args)['show']
    
    sizes, start_config = parse_cisco_file(start)
    sizer, run_config = parse_cisco_file(run)
    
    print(f'Размер файла {start}: {sizes}')
    if show:
        for s in start_config:
            print(s, end='')
    print()
    print(f'Размер файла {run}: {sizer}')
    if show:
        for s in run_config:
            print(s, end='')
    print()
    added = compare(start_config, run_config)
    if len(added) > 0:
        print('Добавленные в конфиг строки: ')
        for s in added:
            print(s)

    remowed = compare(run_config, start_config)
    if len(remowed) > 0:
        print('Удаленные из конфига строки: ')
        for s in remowed:
            print(s)

    if len(added) == 0 and len(remowed) == 0:
        print('Файлы идентичны') 


def parse_cisco_file(path: str) -> Tuple:
    
    patterns = [r'Current configuration : (?P<size>\d+) bytes', r'Using (?P<size>\d+) out of \d+ bytes']
    with open(path, 'r') as filez:
        size = -1
        
        for s in filez:
            if re.match(patterns[0], s):
                size = re.match(patterns[0], s).group('size')
                break
            if re.match(patterns[1], s):
                size = re.match(patterns[1], s).group('size')
                break
        
        config = []
        header = ''
        content = ''

        for s in filez:
            if re.match(r'end', s):
                config.append(header + content)
                break
            elif s[0] != '!' and s[0] != ' ' and len(s) > 0:
                config.append(header + content)
                header = s
                content = ''              
            elif s[0] == ' ':
                content += s

    return size, config[1:]                


def compare(master: List, config: List) -> List:

    diff = []
    for s in config:
        if s not in master and re.search('\w', s):
            diff.append(s)
    return diff



