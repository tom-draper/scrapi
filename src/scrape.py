import requests
from bs4 import BeautifulSoup

def request_url(url: str):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def scrape_img(url: str) -> list[str]:
    soup = request_url(url)
    links = [{'src': a['src'], 'alt': a['alt']} for a in soup.find_all('img')]
    return links


def scrape_link(url: str) -> list[str]:
    soup = request_url(url)
    links = [{'href': a['href']} for a in soup.find_all('a')]
    return links