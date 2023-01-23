from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def request_url(url: str):
    options = Options()
    options.headless = True  # hide GUI
    options.add_argument("--window-size=1920,1080")
    options.add_argument("start-maximized")

    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    driver.get(url)

    return driver


def scrape_img(url: str) -> list[str]:
    driver = request_url(url)
    elements = driver.find_elements(By.TAG_NAME, 'img')
    links = [{'src': element.get_property('src'),
              'alt': element.get_property('alt'),
              'height': element.get_property('height'),
              'width': element.get_property('width')}
             for element in elements]
    return links


def scrape_link(url: str) -> list[str]:
    driver = request_url(url)
    elements = driver.find_elements(By.TAG_NAME, 'a')
    links = [{'text': element.text,
              'href': element.get_property('href')}
             for element in elements]
    return links
