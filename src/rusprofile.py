import requests
from bs4 import BeautifulSoup
from loguru import logger
import pandas as pd

def fetch_html(url: str) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
    }

    try:
        response = requests.get(url, headers=headers)
        logger.info("GET {} status={}", url, response.status_code)
        response.raise_for_status()
        return response.text
    except Exception as e:
        logger.exception("Ошибка при запросе к сайту {}: {}", url, e)
        return ""

def get_okved_main(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        col = soup.find("div", class_="rightcol")
        row = col.find("div", class_="company-row")
        result = row.find("span", class_="company-info__text")
    except Exception:
        logger.exception("Ошибка при получении ОКВЭД: не найдено!")
        return pd.NA

    return result.get_text(strip=True)
