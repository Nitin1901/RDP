from selenium import webdriver

driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://math.iitm.ac.in/people/Faculty")

final = []
fac_links = []
fac_names = []
fac_phone = []
fac_des = []
cards = driver.find_elements_by_class_name('each-user')
for card in cards:
    link = card.get_attribute('data-href')
    print(link)
    fac_links.append(link.strip())
    items = card.find_elements_by_tag_name('p')
    fac_names.append(items[0].text)
    fac_des.append(items[1].text)
    fac_phone.append(items[2].text.strip())

for link,name,phone,designation in zip(fac_links,fac_names,fac_phone,fac_des):
    driver.get(link)
    div = driver.find_element_by_class_name('wrapper')
    items = div.find_elements_by_tag_name('p')
    print(name)
    interests = items[1].text
    interests = [x.strip() for x in interests.split(',')]
    print(designation)
    print(phone)
    print(interests)
    print(link)
    print('\n')

    row = {
        "name": name,
        "contact": {
            "email": None, 
            "ph_num": phone
        },
        "affiliations": [{
            "designation": designation,
            "university": "IIT, Madras",
            "department": "Mathematics"
        }],
        "education": None,
        "profile": link,
        "website":None,
        "interests": interests,
        "experience": None
    }
    final.append(row)

print(final)  

driver.quit()

from pymongo import MongoClient

client = MongoClient("<URI string>")
db = client["RDP"]
collection = db["Professor"]
result = collection.insert_many(final)
print(result)