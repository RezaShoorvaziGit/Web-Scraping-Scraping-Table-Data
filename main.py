
# Import necessary packages
from bs4 import BeautifulSoup
import requests
import re
import json

url = "https://www.yasa.co/national-code-and-issuing-city/"

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")

gdp = soup.find_all("table", attrs={"class": "table--bordered"})

table1 = gdp[0]

body = table1.find_all("tr")

head = body[0]
body_rows = body[1:]


all_rows = []
for row_num in range(len(body_rows)):
    row = []

    for row_item in body_rows[row_num].find_all("td"):

        aa = re.sub("(\xa0)|(\n)|,", "", row_item.text)

        row.append(aa)

    all_rows.append(row)
    
jsonarray = {}
for Key, Value in all_rows:
    jsonarray[Key] = Value
    with open("nationalCodeIR.json", "w") as outfile:
        json.dump(jsonarray, outfile)
