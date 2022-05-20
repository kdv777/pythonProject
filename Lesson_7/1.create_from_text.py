from os import mkdir, makedirs, getcwd, chdir, rename, remove, rmdir
from os.path import join, exists, abspath
from shutil import copy, copy2, copytree, rmtree,move
#

prefix_name = "lesson_7"
main_dir = "my_project"
sub_dirs = ["settings", "mainapp", "adminapp", "authapp" ]
files = ["file1.txt", "file2.bin", "file3.bin","file12.bin" ]

# Сразу создать весь путь
main_path = join(".", prefix_name, main_dir)
if not exists(main_path): makedirs(main_path)
makedirs(join(".", prefix_name, "my_project_2"), exist_ok=True)

main_path_abs = abspath(main_path)
# chdir(main_path_abs) # смена текущей директории

# Создавать последовательно каждый уровень вложенности
for sub_dir in sub_dirs:
    sub_path = join(".", prefix_name, main_dir, sub_dir)
    if not exists(sub_path): mkdir(sub_path)
# Когда создаем файл, предпологаем, что в него надо что-то записать. Даже если 0 байт.
for file in files:
    sub_path = join(".", prefix_name, main_dir, file)
    with open(sub_path, encoding="UTF-8", mode="w"):
        pass

# Удаление
# rmdir(join(".", prefix_name, "my_project_2"))
# chdir(main_path)
# remove("file12.bin")

# Высокоуровневые операции
# move("my_project", new_name)
# copytree("dddd","newn")