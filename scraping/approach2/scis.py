import requests

# download the webpage
page = requests.get("https://scis.uohyd.ac.in/faculty_scis.php", verify=False)
print(page.status_code) # returned 200 (OK)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify()) # print HTML 
        
final = [] # array of records 

# extracting data from tags
fac_basic = soup.find_all(class_="td_faculty")
fac_phd = soup.find_all("font", attrs={"size": "-1"})
fac_email = soup.find_all("td", attrs={"valign": "top", "align": "right"})
fac_interests = soup.find_all("b")

for i, j, k, l in zip(fac_basic, fac_phd, fac_email, fac_interests):
    temp = i.select('b')[0].get_text().strip().split('(')
    name = temp[0]
    if len(temp) > 1:
        desgn = temp[1][:-1]
    else:
        desgn = None

    temp = i.select('a')
    if len(temp) > 1:
        website = temp[1]["href"]
    else:
        website = None
    profile = f'http://scis.uohyd.ac.in/{temp[0]["href"]}'

    temp = i.select("td")[1].get_text().split(':')[1].strip()
    if temp != '':
        ph_num = temp
    else:
        ph_num = None

    phd = j.get_text()
    email = k.get_text().split('\\')[0].strip()

    if 'Areas of Interest' in i.text:
        area = i.next_sibling
        area = " ".join(area.split())
        area = area.split(',')
        area = [i.strip().lower() for i in area]
        area[-1] = area[-1].replace('.', '')

    # single record following schema
    row = {
        "name": name,
        "contact": {
            "email": email, 
            "ph_num": ph_num
        },
        "affiliations": [{
            "designation": desgn,
            "university": "University of Hyderabad",
            "department": "Computer Science"
        }],
        "education": phd,
        "profile": profile,
        "website": website,
        "interests": area,
        "experience": None
    }

    final.append(row)

from pymongo import MongoClient

client = MongoClient("<URI string>") # connect to the db server
db = client["RDP"] # use RDP db
collection = db["Professor"] # use Professor collection
result = collection.insert_many(final) # insert the array of records
print(result) 
