from selenium import webdriver
import time

driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://iitd.irins.org/profile/42893")

image_file = None
image = driver.find_elements_by_tag_name('img')
for i in image:
    print(i.get_attribute('src'))

# publications_lt = []
# sidenav = driver.find_elements_by_class_name('list-group-item')
# if len(sidenav) > 0:
#     for item in sidenav:
#         print(item.text)
#         if item.text.lower() == 'publications':
#             link = item.find_element_by_tag_name('a')
#             if link:
#                 link = link.get_attribute('href')
#                 print(link)
#                 driver.get(link)
#                 time.sleep(5)
#                 publications = driver.find_elements_by_class_name('funny-boxes')
#                 if len(publications) > 0:
                    
#                     for publication in publications:
#                         title = None
#                         authors = None
#                         type = None
#                         journal = None
#                         volume = None
#                         year = None
#                         title = publication.find_element_by_tag_name('h2')
#                         print(title.text)
#                         authors = publication.find_element_by_tag_name('p')
#                         # authors = authors.text.split(';')
#                         print(authors.text)
#                         elements = publication.find_element_by_class_name('label-info')
#                         type = elements.text
#                         print("type: "+ type)
#                         remaining_text = publication.text
#                         remaining_text = remaining_text.replace(title.text, "")
#                         remaining_text = remaining_text.replace(authors.text, "")
#                         remaining_text = remaining_text.replace(type, "")
#                         remaining_text = remaining_text.split("\n")
#                         for i in remaining_text:
#                             if i:
#                                 print(i)
#                                 l = i.split(",")
#                                 l = [i.strip().lower() for i in l]
#                                 print(l)
#                                 journal = l[0]
#                                 for j in l[1:]:
#                                     x = j.split(' ')
#                                     if x[0].lower() == 'volume' and len(x)>1:
#                                         volume = x[1]
#                                     elif x[0].lower() == 'year' and len(x)>1:
#                                         year = x[1]
#                                 break
#                         # print(remaining_text)
#                         print("journal: "+ journal)
#                         print(volume)
#                         print(year)
#                         print()
#                         publication_item = {
#                             "title": title.text,
#                             "authors": authors.text.split(';'),
#                             "type": type,
#                             "journal": journal,
#                             "volume": volume,
#                             "year": year
#                         }
#                         publications_lt.append(publication_item)


# print(publications_lt)
driver.quit()