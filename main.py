import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info

save_info('Старт')


command = sys.argv[1]

if command == 'list':
  get_list()
elif command == 'create_file':
  name = sys.argv[2]
  create_file(name)
elif command == 'create_folder':
  name = sys.argv[2]
  create_folder(name)
elif command == 'delete':
  name = sys.argv[2]
  delete_file(name)
elif command == 'copy':
  name = sys.argv[2]
  new_name = sys.argv[3]
  copy_file(name, new_name)
elif command == 'help':
  print('Помощь')

save_info('конец')