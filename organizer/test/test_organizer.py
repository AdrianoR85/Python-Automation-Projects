import unittest
import tempfile
from pathlib import Path
from organizer import get_path, create_folder, move_file

class TestOrganizer(unittest.TestCase):

  def test_get_path_existing(self):
     temp_dir = tempfile.gettempdir()
     path = get_path(temp_dir)
     self.assertTrue(path.exists())


  def test_get_path_no_existing(self):
     with self.assertRaises(FileNotFoundError):
        get_path("/caminho/que/nao/existe")


  def test_create_folder(self):
    with tempfile.TemporaryDirectory() as temp_dir:
      new_folder = Path(temp_dir) / 'TEST_FOLDER'
      self.assertFalse(new_folder.exists())
      create_folder(new_folder)
      self.assertTrue(new_folder.exists())


  def test_move_file(self):
     with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        origin = base / "arquivo.txt"
        destination_folder = base / "TXT" 

        origin.write_text("conteúdo de teste")
        create_folder(destination_folder)

        move_file(destination_folder, origin)

        file_in_folder = list(destination_folder.glob("*.txt"))
        self.assertEqual(len(file_in_folder), 1)
        self.assertTrue(file_in_folder[0].read_text(), "conteúdo de teste")


if __name__ == '__main__':
   unittest.main()