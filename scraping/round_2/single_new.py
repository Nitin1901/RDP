from selenium import webdriver
import time

driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://jncasr.irins.org/profile/2645")

faculty = []


# time.sleep(20)
# border_elements = driver.find_elements_by_class_name('border_box')
# cit_elements = driver.find_elements_by_class_name('cit_count')

citations = None

#code to scrape the citations and h-index according to google scholar element
# if(len(cit_elements) > 0):
#     citations = {
#         "count": cit_elements[0].text,
#         "h-index": cit_elements[2].text
#     }
i = 0

#code to scrape all ids(scopus, orcid, google scholar)
research_id_el = driver.find_element_by_id('identity-view')
ids = research_id_el.find_elements_by_class_name('notification')
professor_id = dict()
if len(ids) > 0:
    for id in ids:
        id_link = id.find_element_by_tag_name('a').get_attribute('href')
        print(id_link)
        txt = id.text.split('\n')
        professor_id[txt[0]] = txt[1]

print(professor_id)

sidenav = driver.find_elements_by_class_name('list-group-item')
if len(sidenav) > 0:
    for item in sidenav:
        print(item.text)
        if item.text.lower() == 'publications':
            link = item.find_element_by_tag_name('a')
            if link:
                link = link.get_attribute('href')
                print(link)
                driver.get(link)
                time.sleep(10)
                publications = driver.find_elements_by_class_name('funny-boxes')
                if len(publications) > 0:
                    for publication in publications:
                        print(publication.text)
                        print()


# print(citations)
# print(personal_link)
driver.quit()