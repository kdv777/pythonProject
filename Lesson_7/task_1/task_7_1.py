# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
#
# |--my_project
# |   |--settings
# |   |--mainapp
# |   |--adminapp
# |   |--authapp

import os

# Решение в "лоб"
dir_path1 = 'my_project'
if not os.path.exists(dir_path1):
    os.mkdir(dir_path1)
dir_list = ['settings', 'mainapp', 'adminapp', 'authapp']
for el in dir_list:
    dir_path2 = os.path.join(dir_path1, el)
    if not os.path.exists(dir_path2):
        os.mkdir(dir_path2)
