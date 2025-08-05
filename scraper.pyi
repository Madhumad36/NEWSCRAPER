
import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")


# This can vary, so we use common tags seen for headlines
headlines = soup.find_all("a")

with open("headlines.txt", "w", encoding="utf-8") as file:
    for tag in headlines:
        text = tag.get_text().strip()
        if text and len(text) > 40:  # filter short menu links etc.
            file.write(text + "\n")

print("✅ TOI headlines saved to headlines.txt")


