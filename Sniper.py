import random
import requests

def generate_username():
    return ''.join(random.choices([chr(i) for i in range(97, 123)] + [str(i) for i in range(10)], k=4))

def is_username_available(username):
    response = requests.get(f'https://www.instagram.com/{username}/?__a=1')
    if response.status_code == 200:
        return False
    return True

generated_usernames = []
while True:
    username = generate_username()
    if username in generated_usernames:
        continue
    else:
        if is_username_available(username):
            with open('available_usernames.txt', 'a') as f:
                f.write(username + '\n')
            print("Generated username:", username)
        else:
            generated_usernames.append(username)
