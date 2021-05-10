import requests
from bs4 import BeautifulSoup

def get_soup(url : str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

soup = get_soup('https://www.kali.org/')

tags = soup('a')

print("si quieres ser hacker, usa estos links papu: ")

for tag in tags : print(tag.get('href'))
