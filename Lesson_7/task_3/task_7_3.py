# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates:
#
# |--my_project
# ...
# |--templates
# |   |--mainapp
# |   |  |--base.html
# |   |  |--index.html
# |   |--authapp
# |   |  |--base.html
# |   |  |--index.html
#
# Техническое задание
#
# Шаблон - это папка templates в исходной структуре папок. Ее уровень в структуре папок может быть любым.
# В папках mainapp, authapp и аналогичных могут быть и другие файлы, с другими раширениями, кроме тех что приведенны в примере.
# Папку templates надо создать внутри исходной директории, в примере - внутри my_project
# Исходные файлы и папки необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён).
# Предусмотреть возможные исключительные ситуации;

from os import makedirs, walk
import shutil
from os.path import join

# Создаем папку для шаблонов
root_dir = 'my_project'
templ_dir = 'templates'
dir_path = join('.', root_dir, 'templates')
makedirs(dir_path, exist_ok=True)

for path, dirs, files in walk(root_dir):
    for dir_ in dirs:
        if dir_ == templ_dir:
            templ_dir_path = join(path, dir_)
            shutil.copytree(templ_dir_path, dir_path, dirs_exist_ok=True)

# Почему-то третье задание, казалось бы такое примитивное, далось тяжелее, чем второе со звездочкой...
# Не сразу понял, как получить путь найденой папки. В итоге сделал как-то так... Возможно не самый изящный вариант
