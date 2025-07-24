from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os

def get_mackolik_data():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    driver.get("https://arsiv.mackolik.com/Genis-Iddaa-Programi")
    time.sleep(8)
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "html.parser")
    matches = []
    for row in soup.select("tr.match-row"):
        cells = row.select("td")
        if len(cells) < 10:
            continue
        maç = cells[1].get_text(strip=True)
        try:
            iy15 = float(cells[4].get_text(strip=True).replace(",", "."))
            ms25 = float(cells[7].get_text(strip=True).replace(",", "."))
            matches.append({"maç": maç, "İY1.5": iy15, "MS2.5": ms25})
        except:
            continue
    return matches
