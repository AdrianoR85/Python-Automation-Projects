from pathlib import Path
import shutil
import sys
from datetime import datetime
import tempfile

# Log file name
LOG_FILE = "organizer_log.txt"

# Appends a message to the log file with a timestamp
def write_log(message):
  with open(LOG_FILE, 'a', encoding='utf-8') as log:
    log.write(f"{datetime.now().isoformat()} - {message}\n")

# Returns a Path object for the provided directory or Downloads by default
def get_path(dir=None):
  if dir:  
    path = Path(dir).expanduser()  # Expands '~' to the user home directory if used
  else:
    path = Path.home() / 'Downloads'  # Defaults to Downloads folder
  
  if not path.exists():
    raise FileNotFoundError(f"Diretório não encontrado: {path}")
  
  return path

# Creates a folder if it does not exist and logs the action
def create_folder(folder_path):
  if not folder_path.exists():
    folder_path.mkdir()
    msg = f'📁 Criada a pasta: {folder_path.parts[-1]}'
    print(msg)
    write_log(msg)

# Moves a file to the target folder, renaming it if a file with the same name exists
def move_file(path_folder, file_name):
  destination = path_folder / file_name.name
  
  # If a file with the same name exists, add a counter to the filename
  counter = 1
  while destination.exists():
    stem = file_name.stem          # Filename without extension
    suffix = file_name.suffix      # File extension
    new_name = f'{stem}_{counter}{suffix}'
    destination = path_folder / new_name
    counter += 1

  # Move the file and log the operation
  shutil.move(str(file_name), str(destination))
  msg = f'✅ Movido: {file_name.name} -> {destination}'
  print(msg)
  write_log(msg)

# Main logic to organize files by extension in the given folder
def file_organizer():
  # Gets folder path from command-line argument, or uses default
  folder = sys.argv[1] if len(sys.argv) > 1 else None

  try:
    path = get_path(folder) 
  except FileNotFoundError as e:
    msg = f'❌ {e}'
    print(msg)
    write_log(msg)
    return

  # Iterates over each file in the folder
  for file in path.iterdir():
    if file.is_file():
      # Extracts file extension or marks it as 'NO_EXT'
      ext = file.suffix[1:].upper() if file.suffix else 'NO_EXT'
      path_folder = path / ext

      try:
        create_folder(path_folder)
        move_file(path_folder, file)
      except (PermissionError, FileNotFoundError, shutil.Error) as e:
        msg = f'❌ Erro ao mover {file.name}: {e}'
        print(msg)
        write_log(msg)

  # Final log message after processing all files
  write_log(f"✔️ Organização concluída: {path}")

# Entry point when running the script directly
if __name__ == '__main__':
  file_organizer()
