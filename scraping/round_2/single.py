from selenium import webdriver
import time

driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://iitd.irins.org/profile/42893")

faculty = []


time.sleep(20)
border_elements = driver.find_elements_by_class_name('border_box')
cit_elements = driver.find_elements_by_class_name('cit_count')

citations = None

if(len(cit_elements) > 0):
    citations = {
        "count": cit_elements[0].text,
        "h-index": cit_elements[2].text
    }
i = 0

if len(border_elements) > 0:
    for i in range(0, len(border_elements)):
        if(border_elements[i].text == 'Publications'):
            i += 1
            publication_info = border_elements[i].text
        if("Citations" in border_elements[i].text and citations == None):
            i += 1
            info = border_elements[i].text.split('\n')
            citations = {
                "count": info[0],
                "h-index": info[2]
            }
        if 'Personal Information' in border_elements[i].text:
            i += 1
            link_el = border_elements[i].find_element_by_tag_name('a')
            personal_link = link_el.get_attribute('href')
        if 'Experience' in border_elements[i].text:
            i += 1
            exp_time = border_elements[i].find_elements_by_class_name('cbp_tmtime')
            exp_labels = border_elements[i].find_elements_by_class_name('cbp_tmlabel')
            for j in range(0, len(exp_time)):
                print(exp_time[j].text +": "+exp_labels[j].text)
        if 'Qualification' in border_elements[i].text:
            i += 1
            qual_time = border_elements[i].find_elements_by_class_name('cbp_tmtime')
            qual_labels = border_elements[i].find_elements_by_class_name('cbp_tmlabel')
            for j in range(0, len(qual_time)):
                print(qual_time[j].text +": "+qual_labels[j].text)
        
        
print(citations)
print(personal_link)
driver.quit()