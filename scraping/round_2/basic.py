from selenium import webdriver


driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://irins.org/irins/a/searchc/search")

faculty = []

if len(driver.find_elements_by_class_name('list-product-description')) > 0:
    rows = driver.find_elements_by_class_name('list-product-description')
    for row in rows:
        info = row.text.split('\n')
        name = info[1]
        designation = info[2]
        university = info[-6]
        dept = info[-7]
        link_el = row.find_element_by_class_name('col-sm-3')
        link = link_el.find_element_by_tag_name('a').get_attribute('href')
        area = info[3]
        interests = info[4].split(',')
        row = {
            "name": name,
            "affiliations": [{
                "designation": designation,
                "university": university,
                "department": dept
            }],
            "education": None,
            "profile": None,
            "profile_picture": None,
            "website": None,
            "research": {
                "area": area,
                "interests": interests
            },
            "experience": None,
            "publications": None,
            "patents": None,
            "projects": None,
            "academic_identity": None
        }
        faculty.append(row)

print(faculty)
driver.quit()