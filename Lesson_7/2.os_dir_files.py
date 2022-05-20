from os import listdir, scandir, walk, chdir, makedirs
from os.path import join, exists, abspath

from shutil import copy, copy2, copytree

prefix_name = "lesson_7"
main_dir = "my_project"
main_path = join(".", prefix_name, main_dir)

main_path_abs = abspath(main_path)
#chdir(main_path_abs) # смена текущей директории

##print(listdir(main_path)) # Список имен
# Итератор по объектам директории (без поддиректорий)
##scan_data = scandir("some_data_adv")
##for item in scan_data:
##    print(item)

# Итератор по объектам директории (включая поддиректории)
##for root, dirs, files in walk(main_path):
##    print(root, dirs, files)


# Использование фильтров на свойства объектов
# Просто скопируем по маске имени.
src_path = join(".", "some_data_adv")
name_filter_path = join(".", "name_filter_bin_files")
makedirs(name_filter_path,exist_ok=True)
scan_data = scandir(src_path)

for item in scan_data:
    if item.is_file() and item.name.endswith(".bin"):
        copy2(join(src_path, item.name), join(name_filter_path, item.name))
        # copy vs copy2
        # Для более продвинутого фильтра на имя использовать fnmatch, glob


name_size_filter_path = join(".", "name_size_filter_bin_files")
makedirs(name_size_filter_path,exist_ok=True)
scan_data = scandir(src_path)

for item in scan_data:
    if item.is_file() and item.name.endswith(".bin") and item.stat().st_size > 50000:
        copy2(join(src_path, item.name), join(name_size_filter_path, item.name))
        # Перевод даты в человекопонятный формат: datetime.fromtimestamp(item.stat().st_atime)
        # сдвиг по времени например так: datetime.now() - timedelta(hours = 10)
        # now = datetime.now()
        # cr_date = datetime.fromtimestamp(item.stat().st_mtime)
        # delta = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=23, hours=0, weeks=0)
        # cr_date + delta <= now
