import tkinter as tk
from api import get_users

class GitHubManagerApp:
  def __init__(self, master):
    self.master = master
    master.title("Gerenciador de Seguidores/Seguindo do GitHub")
    master.geometry("700x550")

    # Variáveis para armazenar o texto dos campos de entrada
    self.git_user = tk.StringVar()
    self.my_token = tk.StringVar()

    # Frame para organizar os campos de entrada
    input_frame = tk.Frame(master, padx=10, pady=10)
    input_frame.pack(fill=tk.X)

    # Rótulo e Campo de Entrada para o Nome de Usuário
    tk.Label(input_frame, text="Nome do usuário do GitHub:").grid(row=0, column=0, sticky=tk.W, pady=2)
    self.git_user_entry = tk.Entry(input_frame, textvariable=self.git_user, width=40)
    self.git_user_entry.grid(row=0, column=1, pady=2)

    # Rótulo e Campo de Entrada para o Token do Usuário
    tk.Label(input_frame, text="Token de Acesso Pessoal do GitHub:").grid(row=1, column=0, sticky=tk.W, pady=2)
    self.my_token_entry = tk.Entry(input_frame, textvariable=self.my_token, width=40)
    self.my_token_entry.grid(row=1, column=1, pady=2)

    # Botão para iniciar a análise
    self.analyze_button = tk.Button(input_frame, text="Analisar Relações do GitHub", command=self.analyze_relations)
    self.analyze_button.grid(row=2, columnspan=2, pady=2)

    # Placeholder para o método analyze_relations que será implementado depois
    self.analyze_relations_called = False

  def analyze_relations(self):
    # Este método será implementado mais adiante
    # Por enquanto, apenas mostra que foi chamado
    self.analyze_relations_called = True
    print(f"Usuário: {self.git_user.get()}")
    print(f"Token: {self.my_token.get()}")