from selenium import webdriver
import time

driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://pu.irins.org/profile/59246")

publications_lt = []
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
                time.sleep(5)
                publications = driver.find_elements_by_class_name('funny-boxes')
                if len(publications) > 0:
                    
                    for publication in publications:
                        title = None
                        authors = None
                        type = None
                        journal = None
                        volumn = None
                        year = None
                        title = publication.find_element_by_tag_name('h2')
                        print(title.text)
                        authors = publication.find_element_by_tag_name('p')
                        # authors = authors.text.split(';')
                        print(authors.text)
                        elements = publication.find_element_by_class_name('label-info')
                        type = elements.text
                        print("type: "+ type)
                        remaining_text = publication.text
                        remaining_text = remaining_text.replace(title.text, "")
                        remaining_text = remaining_text.replace(authors.text, "")
                        remaining_text = remaining_text.replace(type, "")
                        remaining_text = remaining_text.split("\n")
                        for i in remaining_text:
                            if i:
                                # print(i)
                                l = i.split(",")
                                l = [i.strip().lower() for i in l]
                                journal = l[0]
                                volumn = l[1].split(' ')[1]
                                year = l[2].split(' ')[1]
                                break
                        # print(remaining_text)
                        print("journal: "+ journal)
                        print("volumn: "+ volumn)
                        print("year: "+ year)
                        print()
                        publication_item = {
                            "title": title.text,
                            "authors": authors.text.split(';'),
                            "type": type,
                            "journal": journal,
                            "volumn": volumn,
                            "year": year
                        }
                        publications_lt.append(publication_item)


print(publications_lt)
driver.quit()