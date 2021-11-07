from selenium import webdriver
import time

driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://doms.iitm.ac.in/index.php/faculty-research/faculty-members")

final = []
fac_links = []
cards = driver.find_elements_by_class_name('favpromote')
for card in cards:
    link = card.find_element_by_tag_name('a')
    print(link.get_attribute('href'))
    fac_links.append(link.get_attribute('href'))

for link in fac_links:
    driver.get(link)
    name = driver.find_element_by_class_name('sppb-person-name')
    designation = driver.find_element_by_class_name('sppb-person-designation')
    email = driver.find_element_by_class_name('sppb-person-email')
    name = name.text
    designation = designation.text
    email = email.text
    interests = []
    if len(driver.find_elements_by_class_name('sppb-panel-title')) > 0:
        items = driver.find_elements_by_class_name('sppb-panel-title')
        panel = driver.find_elements_by_class_name('sppb-panel-body')
        k=0
        for i in items:
            if 'Interest' in i.text:
                # i.click()
                driver.execute_script("arguments[0].click();", i)
                time.sleep(5)
                if len(panel[k].find_elements_by_tag_name('ul'))>0:
                    points = panel[k].find_elements_by_tag_name('ul')
                    points = points[len(points)-1].find_elements_by_tag_name('li')
                    for point in points:
                        # print(point.text)
                        interests.append(point.text)
                    break
            k+=1
    
    print(name)
    print(designation)
    print(email)
    print(link)
    print(interests)
    print('\n')


    row = {
        "name": name,
        "contact": {
            "email": email, 
            "ph_num": None
        },
        "affiliations": [{
            "designation": designation,
            "university": "IIT, Madras",
            "department": "Management Studies"
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