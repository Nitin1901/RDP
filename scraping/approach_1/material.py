# importing libraries
from selenium import webdriver

# creating web driver using selenium
driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("http://mme.iitm.ac.in/?page_id=276")

# final list is creates to store all the details extracted in json format
final = []

# Crawling all the faculty details of department and getting profile link of each faculty.
fac_links = []
fac_names = []
cards = driver.find_elements_by_class_name('wc-shortcodes-entry-title')
for card in cards:
    link = card.find_element_by_tag_name('a')
    print(link.get_attribute('href'))
    print(link.text)
    fac_links.append(link.get_attribute('href'))
    fac_names.append(link.text)

# Going to each link and finding the required details.
for link,name in zip(fac_links,fac_names):
    link = link[:4]+link[5:]
    driver.get(link)
    designation = driver.find_element_by_tag_name('h4')
    designation = designation.text
    container = driver.find_element_by_class_name('well')
    data = container.find_elements_by_class_name('col-md-6')
    data = data[1].find_elements_by_tag_name('strong')
    if len(data)>=3:
        phone = data[0].text
        email = data[1].text
        website = data[2].text
    else:
        phone = None
        email = None
        website = None
    interests = []
    ints = container.find_elements_by_tag_name('li')
    for l in ints:
        interests.append(l.text)
    # Printing all the details
    print(name)
    print(website)
    print(designation)
    print(interests)
    print(phone)
    print(email)
    print('\n')
    # Creating a row in json format to push into database
    row = {
        "name": name,
        "contact": {
            "email": email, 
            "ph_num": phone
        },
        "affiliations": [{
            "designation": designation,
            "university": "IIT, Madras",
            "department": "Metallurgical and Materials Engineering"
        }],
        "education": None,
        "profile": link,
        "website":website,
        "interests": interests,
        "experience": None
    }
    # pushing each ro to final list
    final.append(row)

print(final)

driver.quit()

# Code to push all the data to database
from pymongo import MongoClient

client = MongoClient("<URI string>")
db = client["RDP"]
collection = db["Professor"]
result = collection.insert_many(final)
print(result)