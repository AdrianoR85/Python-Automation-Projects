import requests, json

def get_users(git_user, relation_type, token=None):
    if relation_type.lower() not in ["followers", "following"]:
        raise ValueError("relation_type deve ser 'followers' ou 'following")
    users = []
    page = 1
    headers = {}

    if token:
        headers["Authorization"] = f"token {token}"

    while True:
        url = f"https://api.github.com/users/{git_user}/{relation_type}?page={page}&per_page=100"
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Error: {relation_type}: {response.status_code}")
            break
        
        data = response.json()
        if not data:
            break
            
        users.extend(data)
        page +=1
        
    return [user["login"] for user in users]
  

def unfollow_users(token, users_to_unfollow):
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    for username in users_to_unfollow:
        print(username)
        url = f"https://api.github.com/user/following/{username}"
        response = requests.delete(url, headers=headers)

        if response.status_code == 204:
            print(f"✅ Deixou de seguir: {username}")
        else:
            print(f"❌ Erro ao deixar de seguir {username}: {response.status_code} - {response.text}")


def follow_users(token, users_to_follow):
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    for username in users_to_follow:
        url = f"https://api.github.com/user/following/{username}"
        response = requests.put(url, headers=headers)

        if response.status_code == 204:
            print(f"✅ Agora você está seguindo: {username}")
        elif response.status_code == 404:
            print(f"❌ Usuário {username} não encontrado.")
        else:
            print(f"⚠️  Erro ao seguir {username}: {response.status_code} - {response.text}")

  --------------------------------------------------------------------------------------------------------

# How to use
token = "ghp_xxxxx..." # Your token here

followers = get_users("seu_username", "followers", token)
followings = get_users("seu_username", "following", token)

users_to_follow = [user for user in followers if user not in followings] # user that you don't follow
users_to_unfollow = [user for user in followings if user not in followers] # users that don't following you

follow_users(token, users_to_follow)
unfollow_users(token, users_to_unfollow)
