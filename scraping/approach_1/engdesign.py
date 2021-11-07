from selenium import webdriver

driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://ed.iitm.ac.in/team.html")

final = []
cards = driver.find_elements_by_class_name('container-fluid')
for card in cards[2:]:
    items = card.find_elements_by_tag_name('p')
    name = items[0].text
    interests = items[1].text
    interests = interests[14:]
    interests = [x.strip() for x in interests.split(',')]
    website = card.find_element_by_tag_name('a')
    print(name)
    print(interests)
    print(website.get_attribute('href'))
    print('\n')
    row = {
        "name": name,
        "contact": {
            "email": None, 
            "ph_num": None
        },
        "affiliations": [{
            "designation": None,
            "university": "IIT, Madras",
            "department": "Engineering Design"
        }],
        "education": None,
        "profile": None,
        "website": website,
        "interests": interests,
        "experience": None
    }
    final.append(row)

print(final)

driver.quit()

from pymongo import MongoClient

client = MongoClient("mongodb+srv://rdp:ETXTQD0ARke4vPqU@cluster0.ttc9e.mongodb.net/RDP?retryWrites=true&w=majority")
db = client["RDP"]
collection = db["Professor"]
result = collection.insert_many(final)
print(result)