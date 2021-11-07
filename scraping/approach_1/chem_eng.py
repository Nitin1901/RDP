from selenium import webdriver


driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
#link for chemical engineering dept faculty page
driver.get("https://che.iitm.ac.in/core-faculty/")
d = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
d.maximize_window()

faculty = []

cols = driver.find_elements_by_class_name('tmm_textblock')

#looping through professor cards
for col in cols:
    name = col.find_element_by_class_name('tmm_fname')
    #extracting name and profile link from the card
    name = name.text
    profile = col.find_element_by_tag_name('a')
    profile = profile.get_attribute('href')
    
    #opening the profile using selenium
    d.get(profile)
    container = d.find_element_by_class_name('w3-third')

    #checking if personal website links exists
    if len(container.find_elements_by_tag_name('a')) > 0:
        web = container.find_elements_by_tag_name('a')
        website = web[0].get_attribute('href')
    else:
        website = None
    container = container.text.split('\n')
    
    if(' ' in container):
        container.remove(' ')

    #extracting designation, email and contact number and research interests
    desgn = container[0]
    email = container[2]
    phone = container[3]
    research = container[-1]
    #splitting the interests according to delimeter
    if(';' in research):
        research = research.split(';')
    else:
        research = research.split(',')
    #appending details to faculty list
    row = {
        "name": name,
        "contact": {
            "email": email, 
            "ph_num": phone
        },
        "affiliations": [{
            "designation": desgn,
            "university": "IIT, Madras",
            "department": "Chemical Engineering"
        }],
        "education": None,
        "profile": profile,
        "website": website,
        "interests": research,
        "experience": None
    }
    faculty.append(row)

print(faculty)
d.quit()
driver.quit()

#pushing recording to mongodb
from pymongo import MongoClient

client = MongoClient("<URI string>")
db = client["RDP"]
collection = db["Professor"]
result = collection.insert_many(faculty)
print(result)