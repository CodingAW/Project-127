import csv
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(start_url)

print(page)
time.sleep(2)

soup = BeautifulSoup(page.text, "html.parser")
star_table = soup.find("table")

temp_list = []
table_rows = star_table.find_all("tr")

for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

star_name = []
star_distance = []
star_mass = []
star_radius = []
star_luminosity = []

for i in range(1, len(temp_list)):
    star_name.append(temp_list[i][1])   
    star_distance.append(temp_list[i][3])  
    star_mass.append(temp_list[i][5]) 
    star_radius.append(temp_list[i][6])
    star_luminosity.append(temp_list[i][7]) 

df2 = pd.DataFrame(list(zip(star_name, star_distance, star_mass, star_radius, star_luminosity)), columns= ["name", "distance", "mass", "radius", "luminosity"])
print(df2)

df2.to_csv("brightstar.csv")