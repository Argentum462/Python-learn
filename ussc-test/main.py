import argparse
import modules.cisco_show as cisco_show
import modules.windows_audit as windows_audit
import modules.windows_secedit as windows_secedit


# Главное меню
main_parser = argparse.ArgumentParser(description='Утилита для обработки данных с ОЗ Cisco Catalyst и Windows')
subparsers = main_parser.add_subparsers(title='Главное меню', help='Режимы разбора')

# Элемент audit
audit_parser = subparsers.add_parser('a', help='Разобрать файл audit')
audit_parser.add_argument('path', help='Путь к файлу аудита')
audit_parser.set_defaults(func = windows_audit.main)

# Элемент secedit
secedit_parser = subparsers.add_parser('s', help='Разобрать файл secedit')
secedit_parser.add_argument('path', help='Путь к файлу политики безопаности')  # Обязательный аргумент
secedit_parser.add_argument('-v', '--verbose', action='store_true', help='Отображать сокращенные значения')  # Опциональный аргумент-флаг
secedit_parser.add_argument('-m', '--max_width', default = 90, help='Максимальная длина значения таблицы (по умолчанию 90)')
secedit_parser.set_defaults(func = windows_secedit.main)

# Элемент Cisco
cisco_parser = subparsers.add_parser('c', help='Сравнить файлы Cisco')
cisco_parser.add_argument('start', help='Путь к файлу start')
cisco_parser.add_argument('run', help='Путь к файлу run')
cisco_parser.add_argument('-s', '--show', action='store_true', help='Вывести содержимое файлов в консоль')
cisco_parser.set_defaults(func = cisco_show.main)

args = main_parser.parse_args()
if len(vars(args)) == 0:
    main_parser.print_help()
else:
    args.func(args)

