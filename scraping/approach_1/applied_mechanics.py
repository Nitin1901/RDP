from selenium import webdriver


driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://apm.iitm.ac.in/faculty.html")

faculty = []

cols = driver.find_elements_by_class_name('col-md-6')


for col in cols:
    section = col.find_element_by_tag_name('section')
    panel = section.find_element_by_class_name('panel-body')
    n = panel.find_element_by_tag_name('h3')
    
    name = n.text[:n.text.find('\n')]
    # print(name)
    desgn = n.text[n.text.find('\n')+1:]
    if('Professor' in name):
        temp = name
        name = desgn
        desgn = temp
    profile = panel.find_element_by_tag_name('a')
    profile = profile.get_attribute('href')
    email = panel.text[panel.text.find('Email: ')+7: panel.text.find('\n', panel.text.find('Email: ')+7)]
    email = email.replace('[at]', '@')
    email = email.replace('[.]', '.')
    if(panel.text.find('Phone: ') != -1):
        phone = panel.text[panel.text.find('Phone: ')+7: panel.text.find('\n', panel.text.find('Phone: ')+7)]
    else:
        phone = None
    interest = panel.text[panel.text.find('Area of Interest')+17: ]

    # li = ps[0].find_element_by_tag_name('a')
    row = {
        "name": name,
        "contact": {
            "email": email, 
            "ph_num": phone
        },
        "affiliations": [{
            "designation": desgn,
            "university": "IIT, Madras",
            "department": "Applied Mechanics"
        }],
        "education": None,
        "profile": profile,
        "website": None,
        "interests": interest.split('\n'),
        "experience": None
    }
    faculty.append(row)
del(faculty[0])

print(faculty)
driver.quit()

from pymongo import MongoClient

client = MongoClient("<URI string>")
db = client["RDP"]
collection = db["Professor"]
result = collection.insert_many(faculty)
print(result)