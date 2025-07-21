import tkinter as tk
from api import get_users

class GitHubManagerApp:
  def __init__(self, master):
    self.master = master
    master.title("Gerenciador de Seguidores/Seguindo do GitHub")
    master.geometry("580x550")

    # Variáveis para armazenar o texto dos campos de entrada
    self.git_user = tk.StringVar()
    self.my_token = tk.StringVar()

    # Listas para armazenar os dados (inicialmente vazias)
    self.users_to_follow = []
    self.users_to_unfollow = []

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

    # Frame para os resultados (Listboxes)
    result_frame = tk.Frame(master, padx=10, pady=10)
    result_frame.pack(fill=tk.BOTH, expand=True)

    # Usuários a Seguir (LabelFrame e Listbox)
    follow_frame = tk.LabelFrame(result_frame, text="Usuários a Seguir", padx=5, pady=5)
    follow_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    self.follow_listbox = tk.Listbox(follow_frame, height=15, width=40)
    self.follow_listbox.pack(fill=tk.BOTH, expand=True)

    # Botão para seguir
    self.follow_buttom = tk.Button(follow_frame, text="Seguir Todos Exibidos", command=self.perform_follow)
    self.follow_buttom.pack(pady=5)

    # Usuários a Deixar de Seguir (LabelFrame e Listbox)
    unfollow_frame = tk.LabelFrame(result_frame, text="Usuários para deixar de Seguir", padx=5, pady=5)
    unfollow_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    self.unfollow_listbox = tk.Listbox(unfollow_frame, height=15, width=40)
    self.unfollow_listbox.pack(fill=tk.BOTH, expand=True)

    # Botão para deixar de seguir
    self.unfollow_buttom = tk.Button(unfollow_frame, text="Deixar de Seguir Todos Exibidos", command=self.perform_unfollow)
    self.unfollow_buttom.pack(pady=5)

    # Configurações para que os frames e listboxes se expandam com a janela
    result_frame.grid_columnconfigure(0, weight=1)
    result_frame.grid_columnconfigure(1, weight=1)
    result_frame.grid_rowconfigure(0, weight=1)


  def analyze_relations(self):
    # Simula o preenchimento das listas para testar a GUI
    self.users_to_follow = ["userA", "userB", "userC"]
    self.users_to_unfollow = ["userX", "userY"]
    self.update_listboxes()
    print("Listas atualizadas (simulado).")

  def update_listboxes(self):
    """Atualiza as Listboxes com os usuários a seguir e a deixar de seguir."""
    self.follow_listbox.delete(0, tk.END) # Limpa a listbox antes de adicionar novos itens
    for user in self.users_to_follow:
      self.follow_listbox.insert(tk.END, user) # Adiciona cada usuário ao final da listbox

    self.unfollow_listbox.delete(0,tk.END)
    for user in self.users_to_unfollow:
      self.unfollow_listbox.insert(tk.END, user)
  
  def perform_follow(self):
    print("Botão 'Seguir Todos Exibidos' clicado!")
    print(f"Usuários a seguir: {self.users_to_follow}")
    self.users_to_follow = []
    self.update_listboxes()

  def perform_unfollow(self):
    print("Botão 'Deixar de Seguir Todos Exibidos' clicado!")
    print(f"Usuários a deixar de seguir: {self.users_to_unfollow}")
    self.users_to_unfollow = []
    self.update_listboxes()