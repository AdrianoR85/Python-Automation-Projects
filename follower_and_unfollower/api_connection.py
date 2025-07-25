import requests

def get_users(git_user, relation_type, token=None, status_callback=None):
    if relation_type.lower() not in ["followers", "following"]:
        raise ValueError("relation_type deve ser 'followers' ou 'following")
    
    users = []
    page = 1
    headers = {}

    if token:
        headers["Authorization"] = f"token {token}"

    if status_callback:
        status_callback(f"Buscando {relation_type} para {git_user}...")


    while True:
        url = f"https://api.github.com/users/{git_user}/{relation_type}?page={page}&per_page=100"
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            msg = f"Error ao buscar {relation_type}: {response.status_code} - {response.text}"
            if status_callback:
                status_callback(msg)
            raise requests.exceptions.RequestException(msg)
        
        data = response.json()
        if not data:
            break
            
        users.extend(data)
        page +=1

    if status_callback:
        status_callback(f"Busca de {relation_type} finalizada. Encontrados {len(users)} usúarios.")

    return [user["login"] for user in users]
  

def unfollow_users(token, users_to_unfollow, status_callback=None):
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    for username in users_to_unfollow:
        url = f"https://api.github.com/user/following/{username}"
        
        response = requests.delete(url, headers=headers)

        if response.status_code == 204:
            msg = f"✅ Deixou de seguir: {username}"
            if status_callback:
                status_callback(msg)
        
        else:
            msg = f"❌ Erro ao deixar de seguir {username}: {response.status_code} - {response.text}"
            if status_callback:
                status_callback(msg)
             

def follow_users(token, users_to_follow, status_callback=None):
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    for username in users_to_follow:
        url = f"https://api.github.com/user/following/{username}"
        response = requests.put(url, headers=headers)

        if response.status_code == 204:
            msg = f"✅ Agora você está seguindo: {username}"
            if status_callback:
                status_callback(msg)
            # raise requests.exceptions.RequestException(msg)
        
        elif response.status_code == 404:
            msg = f"❌ Usuário {username} não encontrado."
            if status_callback:
                status_callback(msg)
            # raise requests.exceptions.RequestException(msg)    
        else:
            msg = f"⚠️  Erro ao seguir {username}: {response.status_code} - {response.text}"
            if status_callback:
                status_callback(msg)
            # raise requests.exceptions.RequestException(msg)