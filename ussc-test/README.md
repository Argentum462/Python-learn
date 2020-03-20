# Config_parser

Собранный контейнер: https://hub.docker.com/repository/docker/argentum462/config_parser


Функционал (режимы разбора имеют собственные help-страницы):

```bash
usage: main.py [-h] {a,s,c} ...

Утилита для обработки данных с ОЗ Cisco Catalyst и Windows

optional arguments:
  -h, --help  show this help message and exit

Главное меню:
  {a,s,c}     Режимы разбора
    a         Разобрать файл audit
    s         Разобрать файл secedit
    c         Сравнить файлы Cisco
```


Пример запуска утилиты из командной строки:

```bash
python3 main.py c configs/Show_start.txt configs/Show_run.txt 

Размер файла Show_start.txt: 3362

Размер файла Show_run.txt: 3362

Добавленные в конфиг строки: 
vlan 3
 name Manage

```


Пример запуска утилиты в контейнере с передачей двух конфигов Cisco из текущего каталога:

```bash
docker run -v "$(pwd)"/Show_start.txt:/Show_start.txt \
-v "$(pwd)"/Show_run.txt:/Show_run.txt \
argentum462/config_parser c Show_start.txt Show_run.txt

Размер файла Show_start.txt: 3362

Размер файла Show_run.txt: 3362

Добавленные в конфиг строки: 
vlan 3
 name Manage

```

