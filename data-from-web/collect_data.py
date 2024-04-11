import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get("https://www.larrysballet.com/")
soup = BeautifulSoup(page.content, "html.parser")
h2s = soup.find_all("h2")

studios = [h2.get_text() for h2 in h2s]

print(studios)

studios = pd.DataFrame({"studios": studios})
print(studios.head())


studios.to_csv("studios.csv")
