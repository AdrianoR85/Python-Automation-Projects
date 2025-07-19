import tkinter as tk
from github_manager import GitHubManagerApp

if __name__ == "__main__":
  root = tk.Tk()
  app = GitHubManagerApp(root)
  root.mainloop()