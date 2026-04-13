import requests
import string
import os
from bs4 import BeautifulSoup

HEADERS = {"Accept-Language": "en-US,en;q=0.5"}

def clean_filename(title):
    translator = str.maketrans("", "", string.punctuation)
    title = title.translate(translator)
    return title.strip().replace(" ", "_")

def get_article_text(article_url):
    response = requests.get(article_url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    # різні типи статей мають різні контейнери
    body = (
        soup.find("div", {"class": lambda c: c and "body" in c})
        or soup.find("div", {"class": lambda c: c and "article" in c})
    )
    if body:
        return body.get_text(separator="\n").strip()
    return None

num_pages   = int(input("> ").strip())
article_type = input("> ").strip()

for page_num in range(1, num_pages + 1):
    url = f"https://www.nature.com/nature/articles?sort=PubDate&year=2022&page={page_num}"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    folder = f"Page_{page_num}"
    os.makedirs(folder, exist_ok=True)

    articles = soup.find_all("article")

    for article in articles:
        type_tag = article.find("span", {"data-test": "article.type"})
        if not type_tag or type_tag.text.strip() != article_type:
            continue

        link_tag = article.find("a", {"data-track-action": "view article"})
        if not link_tag:
            continue

        title       = link_tag.text.strip()
        article_url = "https://www.nature.com" + link_tag["href"]
        text        = get_article_text(article_url)

        if not text:
            continue

        filename = os.path.join(folder, clean_filename(title) + ".txt")
        with open(filename, "wb") as f:
            f.write(text.encode("utf-8"))

print("Saved all articles.")