from selenium import webdriver


driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
#link for CSE dept faculty page
driver.get("http://www.cse.iitm.ac.in/listpeople.php?arg=MSQw")

d = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
d.maximize_window()

def get_personal_website(link):
    d.get(link)
    if len(d.find_elements_by_class_name('aclass')) > 0:
        webs = d.find_elements_by_class_name('aclass')
        for web in webs:
            if(web.text == 'Link to Personal Homepage'):
                print(web.get_attribute('href'))
    return web.get_attribute('href')

faculty = []


if len(driver.find_elements_by_id('homepage')) > 0:
    container = driver.find_element_by_id('homepage')
    table = container.find_element_by_tag_name('tbody')
    rows = table.find_elements_by_tag_name('tr')
    del(rows[0])
    #looping through the rows in the table
    for row in rows:
        cols = row.find_elements_by_tag_name('td')
        for col in cols:
            #chhecking if the column contains content or is an image
            if len(col.find_elements_by_tag_name('span')) > 0:
                #extracting profile link
                prof1 = col.find_element_by_tag_name('span')
                web1 = prof1.find_element_by_tag_name('a')
                link1 = web1.get_attribute('href')
                #opening the profile page
                website = get_personal_website(link1)
                name = prof1.text[0: prof1.text.index('(')]
                phone = prof1.text[prof1.text.find('Phone :')+7: prof1.text.find('\n', prof1.text.find('Phone :')+7)]
                desgn = prof1.text[prof1.text.index('(')+1: prof1.text.index(')')]
                #formatting email
                email = prof1.text[prof1.text.find('Email : ')+8:prof1.text.find('\n', prof1.text.find('Email : ')+8)]
                email = email.replace(' [at] ', '@')
                email = email.replace(' [dot] ', '.')
                research = prof1.text[prof1.text.find('Research Interests : ')+21:prof1.text.find('\n', prof1.text.find('Research Interests : ')+21)]
                
                #appending details to faculty list
                row = {
                    "name": name,
                    "contact": {
                        "email": email, 
                        "ph_num": "044-2257-"+phone if phone else None
                    },
                    "affiliations": [{
                        "designation": desgn,
                        "university": "IIT, Madras",
                        "department": "Computer Science Engineering"
                    }],
                    "education": None,
                    "profile": link1,
                    "website": website,
                    "interests": research.split(','),
                    "experience": None
                }
                faculty.append(row)
                #print(phone)

print(faculty)
driver.quit()
d.quit()

#pushing recording to mongodb
from pymongo import MongoClient

client = MongoClient("<URI string>")
db = client["RDP"]
collection = db["Professor"]
result = collection.insert_many(faculty)
print(result)