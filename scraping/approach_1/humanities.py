# importing libraries
from selenium import webdriver

# creating web driver using selenium
driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://hss.iitm.ac.in/team-members/")

# final list is creates to store all the details extracted in json format
final = []

# Crawling all the faculty details of department and getting profile link of each faculty.
fac_links = []
cards = driver.find_elements_by_class_name('fg-item')
for card in cards:
    link = card.find_element_by_tag_name('a')
    print(link.get_attribute('href'))
    fac_links.append(link.get_attribute('href'))

# Going to each link and finding the required details.
for link in fac_links:
    driver.get(link)
    name = driver.find_element_by_class_name('page-title')
    name = name.text
    designation = driver.find_elements_by_tag_name('strong')
    for i in designation:
        if i.text!='':
            designation = i.text
            break
    ps = driver.find_elements_by_tag_name('p')
    interests = []
    for p in ps:
        if 'research interest' in p.text.lower():
            if len(p.find_elements_by_xpath("./following-sibling::ul"))>0:
                ul = p.find_element_by_xpath("./following-sibling::ul")
                li = ul.find_elements_by_tag_name('li')
                for i in li:
                    interests.append(i.text)
            break
    # Printing all the details
    print(name)
    print(designation)
    print(link)
    print(interests)
    print('\n')
    # Creating a row in json format to push into database
    row = {
        "name": name,
        "contact": {
            "email": None, 
            "ph_num": None
        },
        "affiliations": [{
            "designation": designation,
            "university": "IIT, Madras",
            "department": "Humanities and Social Sciences"
        }],
        "education": None,
        "profile": link,
        "website":None,
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