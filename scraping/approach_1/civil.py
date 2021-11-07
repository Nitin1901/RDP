from selenium import webdriver
import time

driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://civil.iitm.ac.in/faculty.php")

faculty = []

content = driver.find_elements_by_class_name('main-content')
profs = driver.find_elements_by_class_name('selector')
for prof in profs:
    driver.execute_script("arguments[0].click();", prof)
    # prof.click()
    time.sleep(5)
    cont = driver.find_element_by_id('feedBk')
    # print(cont.text)
    text = cont.text.split('\n')
    name = text[0]
    education = text[1]
    education = education[1:-1]
    desgn = text[2]
    contact_detail = text[4].split(' | ')
    email = None
    phone = None
    # phone = contact_detail[1]
    # email = contact_detail[2]
    for c in contact_detail:
        if '@' in c and email == None:
            email = c
        if '+91' in c:
            phone = c
    research = text[-1].split(',')
    profile = cont.find_element_by_tag_name('a')
    profile = profile.get_attribute('href')
    inputs = cont.find_elements_by_tag_name('input')
    driver.execute_script("arguments[0].click();", inputs[1])
    # inputs[1].click()
    time.sleep(5)
    row = {
        "name": name,
        "contact": {
            "email": email, 
            "ph_num": phone
        },
        "affiliations": [{
            "designation": desgn,
            "university": "IIT, Madras",
            "department": "Civil Engineering"
        }],
        "education": education,
        "profile": profile,
        "website": None,
        "interests": research,
        "experience": None
    }
    faculty.append(row)


driver.quit()
print(faculty)


from pymongo import MongoClient

client = MongoClient("<URI string>")
db = client["RDP"]
collection = db["Professor"]
result = collection.insert_many(faculty)
print(result)