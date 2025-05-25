from pathlib import Path
import shutil
import sys
from datetime import datetime
import tempfile

LOG_FILE = "organizer_log.txt"

def write_log(message):
  with open(LOG_FILE, 'a', encoding='utf-8') as log:
    log.write(f"{datetime.now().isoformat()} - {message}\n")


def get_path(dir=None):
  if dir:  
    path = Path(dir).expanduser()
  else:
    path = Path.home() / 'Downloads'
  
  if not path.exists():
    raise FileNotFoundError(f"Diretório não encontrado: {path}")
  
  return path


def create_folder(folder_path):
  if not folder_path.exists():
    folder_path.mkdir()
    msg = f'📁 Criada a pasta: {folder_path.parts[-1]}'
    print(msg)
    write_log(msg)


def move_file(path_folder, file_name):
  destination = path_folder / file_name.name
  
  counter = 1
  while destination.exists():
    stem = file_name.stem
    suffix = file_name.suffix
    new_name = f'{stem}_{counter}{suffix}'
    destination = path_folder / new_name
    counter += 1
  
  shutil.move(str(file_name), str(destination))
  msg = f'✅ Movido: {file_name.name} -> {destination}'
  print(msg)
  write_log(msg)


def file_organizer():

  folder = sys.argv[1] if len(sys.argv) > 1 else None

  try:
    path = get_path(folder) 
  except FileNotFoundError as e:
    msg = f'❌ {e}'
    print(msg)
    write_log(msg)
    return

  # Lista todos os arquivos no diretório
  for file in path.iterdir():
    if file.is_file():
      ext = file.suffix[1:].upper() if file.suffix else 'NO_EXT'
      path_folder = path / ext

      try:
        create_folder(path_folder)
        move_file(path_folder, file)
      except (PermissionError, FileNotFoundError, shutil.Error) as e:
        msg = f'❌ Erro ao mover {file.name}: {e}'
        print(msg)
        write_log(msg)

  write_log(f"✔️ Organização concluída: {path}")


if __name__ == '__main__':
  file_organizer()