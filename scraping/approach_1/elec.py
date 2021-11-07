from selenium import webdriver


driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.ee.iitm.ac.in/faculty-members/")

faculty = []


if len(driver.find_elements_by_class_name('su-table-alternate')) > 0:
    tables = driver.find_elements_by_class_name('su-table-alternate')
    table = tables[1].find_element_by_tag_name('tbody')
    rows = table.find_elements_by_tag_name('tr')
    del(rows[0])
    for row in rows:
        cols = row.find_elements_by_tag_name('td')
        if len(cols[1].find_elements_by_tag_name('a')) > 0:
            name = cols[1].find_element_by_tag_name('a')
            link = name.get_attribute('href')
            name = name.text
            # print(name.text)
            # print(link)
        else:
            name = cols[1].text
        phone = cols[2].text
        email = cols[3].text
        research = cols[4].text
        row = {
            "name": name,
            "contact": {
                "email": email+"@ee.iitm.ac.in", 
                "ph_num": "+91 44 2257 "+phone
            },
            "affiliations": [{
                "designation": None,
                "university": "IIT, Madras",
                "department": "Electrical Engineering"
            }],
            "education": None,
            "profile": link,
            "website": None,
            "interests": research.split(','),
            "experience": None
        }
        faculty.append(row)

print(faculty)
driver.quit()

from pymongo import MongoClient

client = MongoClient("<URI string>")
db = client["RDP"]
collection = db["Professor"]
result = collection.insert_many(faculty)
print(result)