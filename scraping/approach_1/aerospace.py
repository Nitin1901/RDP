from selenium import webdriver


driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
#link for aerospace dept faculty page
driver.get("http://www.ae.iitm.ac.in/files/faculty.htm")

faculty = []


if len(driver.find_elements_by_id('content')) > 0:
    container = driver.find_element_by_id('content')
    tables = container.find_elements_by_tag_name('tbody')
    # rows = table.find_elements_by_tag_name('tr')
    #looping through all the tables
    for table in tables:
        #looping each row in the table
        rows = table.find_elements_by_tag_name('tr')
        for row in rows:
            cols = row.find_elements_by_tag_name('td')
            col = cols[1]
            if len(col.find_elements_by_tag_name('li')) > 0:
                els = col.find_elements_by_tag_name('li')
                name = els[0].text
                desgn = els[1].text
                research = els[2].text[19:]
                #trimming the line consisteing email
                email = els[3].text[8: els[3].text.find(' ', 8)]
                if (els[3].text.find('Phone: ') != -1):
                    phone = els[3].text[els[3].text.find('Phone: ')+7:]
                else:
                    phone = None
                #getting link url from anchor tag
                link_el = els[4].find_element_by_tag_name('a')
                link = link_el.get_attribute('href')

                #appending details to faculty list
                row = {
                    "name": name,
                    "contact": {
                        "email": email, 
                        "ph_num": "+91 44 2257 "+phone[-4:] if phone else None
                    },
                    "affiliations": [{
                        "designation": desgn,
                        "university": "IIT, Madras",
                        "department": "Aerospace Engineering"
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

#pushing recording to mongodb
from pymongo import MongoClient

client = MongoClient("<URI string>")
db = client["RDP"]
collection = db["Professor"]
result = collection.insert_many(faculty)
print(result)