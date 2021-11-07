# importing libraries
from selenium import webdriver

# creating web driver using selenium
driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://physics.iitm.ac.in/people/Faculty")

# final list is creates to store all the details extracted in json format
final = []

# Crawling all the faculty details of department and getting profile link of each faculty.
fac_links = []
cards = driver.find_elements_by_class_name('each-user')
for card in cards:
    if(type(card.get_attribute('data-href')) is str):
        print(card.get_attribute('data-href'))
        fac_links.append(card.get_attribute('data-href'))

# Going to each link and finding the required details.
for link in fac_links:
    driver.get(link)
    name = driver.find_element_by_class_name('h3')
    name = name.text
    if len(driver.find_elements_by_class_name('wrapper')) > 0:
        wrap = driver.find_element_by_class_name('wrapper')
        all = wrap.find_elements_by_tag_name('p')
        designation = all[0].text
        education = 'PhD, '+all[1].text
        interests = all[2].text
        interests = [x.strip() for x in interests.split(',')]
        phone = all[3].text
        email = all[4].text
    else:
        designation = None
        education = 'PhD'
        interests = None
        phone = None
        email = None
    profile = link
    website = driver.find_element_by_class_name('inpplpage')
    website = website.get_attribute('href')
    # Printing all the details
    print(website)
    print(designation)
    print(education)
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
            "department": "Physics"
        }],
        "education": education,
        "profile": profile,
        "website":website,
        "interests": interests,
        "experience": None
    }
    # pushing each ro to final list
    final.append(row)

driver.quit()

print(final)

# Code to push all the data to database
from pymongo import MongoClient

client = MongoClient("<URI string>")
db = client["RDP"]
collection = db["Professor"]
result = collection.insert_many(final)
print(result)