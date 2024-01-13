from bs4 import BeautifulSoup as bs
import requests 
import pandas as pd

stars_url = "https://en.wikipedia.org/wiki/List_of_nearest_giant_stars"
page = requests.get(stars_url)
soup = bs(page.text,"html.parser")

star_table = soup.find('table')
temp_list = []
table_rows = star_table.find_all("tr")

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

star_names = []
distance = []
mass = []
radius = []

#print(temp_list)

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][4])

headers = ["star_names","distance","mass","radius"]
df = pd.DataFrame(list(zip(star_names,distance,mass,radius)),columns = headers)
df.to_csv('stars.csv')