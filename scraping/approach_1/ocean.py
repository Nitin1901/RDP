from selenium import webdriver

driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://doe.iitm.ac.in/faculty/")

final = []
fac_links = []
fac_names = []
cards = driver.find_elements_by_class_name('tmm_member')
for card in cards:
    link = card.find_element_by_tag_name('a')
    name = card.find_element_by_class_name('tmm_fname')
    print(link.get_attribute('href'))
    print(name.text)
    fac_links.append(link.get_attribute('href'))
    fac_names.append(name.text)

for link,name in zip(fac_links,fac_names):
    driver.get(link)
    container = driver.find_elements_by_class_name('w3-container')
    container = container[1]
    items = container.find_elements_by_tag_name('p')
    designation = items[0].text
    email = items[2].text
    phone = items[3].text
    if len(items)>=6:
        if items[4].text == 'Research Areas':
            interests = items[5].text
            interests = [x.strip() for x in interests.split(',')]
            if len(items)>=8:
                education = items[7].text
            else:
                education = None
        else:            
            interests = items[6].text
            interests = [x.strip() for x in interests.split(',')]
            if len(items)>=9:
                education = items[8].text
            else:
                education = None
    else:
        interests = None
        education = None

    print(name)
    print(designation)
    print(email)
    print(phone)
    print(interests)
    print(education)
    print(link)
    print('\n')

    row = {
        "name": name,
        "contact": {
            "email": email, 
            "ph_num": phone
        },
        "affiliations": [{
            "designation": designation,
            "university": "IIT, Madras",
            "department": "Ocean Engineering"
        }],
        "education": education,
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