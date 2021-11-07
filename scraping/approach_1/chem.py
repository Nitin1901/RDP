from selenium import webdriver


driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
#link for chemistry dept faculty page
driver.get("http://chem.iitm.ac.in/faculty/")
d = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
d.maximize_window()

faculty = []

container = driver.find_element_by_class_name('gdlr-core-container')
cols = container.find_elements_by_class_name('gdlr-core-column-20')
#looping through professor cards
for col in cols:
    text = col.text.split('\n')
    #extracting name,designation, email, phone and profile link from the card
    name = text[0]
    desgn = text[1]
    email = text[2]
    phone = text[3]
    profile = col.find_element_by_tag_name('a')
    profile = profile.get_attribute('href')

    #opening the profile page
    d.get(profile)
    # main_col = d.find_element_by_class_name('gdlr-core-column-first')
    # content = main_col.find_element_by_class_name('gdlr-core-pbf-column-content')
    rows = d.find_elements_by_class_name('gdlr-core-pbf-element')
    # print(name)
    #extracting education and research
    for i in range (0, len(rows)):
        if(rows[i].text == 'Education'):
            education = rows[i+1].text.split('\n')[0]
            # print(education)
        if(rows[i].text == 'Research Interests'):
            research = rows[i+1].text.split('\n')
            break
            # print(research)
    
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
            "department": "Chemistry"
        }],
        "education": education,
        "profile": profile,
        "website": None,
        "interests": research,
        "experience": None
    }
    faculty.append(row)
    
    # if(len(rows) == 1):
    #     print(rows[0].text)



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