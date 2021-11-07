from selenium import webdriver


driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()

#link for biotechnology dept faculty page
driver.get("https://biotech.iitm.ac.in/faculty/")
d = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
d.maximize_window()

faculty = []

content = driver.find_element_by_id('regular')
cols = content.find_elements_by_class_name('card__people-content')

#looping through professor cards
for col in cols:
    info = col.text.split('\n')
    #extracting name, designation, profile link and ressearch interest from card
    name = info[0]
    desgn = info[1]
    profile = col.find_element_by_tag_name('a')
    profile = profile.get_attribute('href')
    research = col.find_element_by_class_name('card__people-research')
    research = research.text.split(',')

    #opening the profile link to get education, email and phone details
    d.get(profile)
    info = d.find_element_by_class_name('people-single-content')
    education = info.find_element_by_class_name('degrees')
    education = education.text
    personal = info.find_element_by_class_name('single-body-content')
    personal = personal.text.split('\n')
    for p in personal:
        if '@' in p:
            email = p
        if '+91-44' in p:
            phone = p
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
            "department": "Biotechnology"
        }],
        "education": education,
        "profile": profile,
        "website": None,
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