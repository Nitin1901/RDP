from selenium import webdriver
import time

driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://pu.irins.org/profile/22965")

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

# if len(border_elements) > 0:
#     for i in range(0, len(border_elements)):
#         if(border_elements[i].text == 'Publications'):
#             i += 1
#             publication_info = border_elements[i].text
#         # if("Citations" in border_elements[i].text and citations == None):
#         #     i += 1
#         #     info = border_elements[i].text.split('\n')
#         #     citations = {
#         #         "count": info[0],
#         #         "h-index": info[2]
#         #     }
#         if 'Personal Information' in border_elements[i].text:
#             i += 1
#             link_el = border_elements[i].find_elements_by_tag_name('a')
#             if len(link_el) > 0:
#                 personal_link = link_el[0].get_attribute('href')
#         if 'Experience' in border_elements[i].text:
#             i += 1
#             exp_time = border_elements[i].find_elements_by_class_name('cbp_tmtime')
#             exp_labels = border_elements[i].find_elements_by_class_name('cbp_tmlabel')
#             for j in range(0, len(exp_time)):
#                 print(exp_time[j].text +": "+exp_labels[j].text)
#         if 'Qualification' in border_elements[i].text:
#             i += 1
#             qual_time = border_elements[i].find_elements_by_class_name('cbp_tmtime')
#             qual_labels = border_elements[i].find_elements_by_class_name('cbp_tmlabel')
#             for j in range(0, len(qual_time)):
#                 print(qual_time[j].text +": "+qual_labels[j].text)


#new method
#scrape expertise
if len(driver.find_elements_by_id('expertise-view')) > 0:
    exp_el = driver.find_element_by_id('expertise-view')
    area_el = driver.find_elements_by_id('e_expertise')
    if len(area_el) > 0:
        area = area_el[0].text
    interest_el = driver.find_elements_by_id('e_s_expertise')
    if len(interest_el) > 0:
        interest = interest_el[0].text.split(',')
print(area)
print(interest)
#personal info
if len(driver.find_elements_by_id('list_panel_personal')) > 0:
    personal_info = driver.find_element_by_id('list_panel_personal')
    link_el = personal_info.find_elements_by_tag_name('a')
    if len(link_el) > 0:
        personal_link = link_el[0].get_attribute('href')
    print(personal_link)
#list of experience
if len(driver.find_elements_by_id('exp-ul')) > 0:
    exp_el = driver.find_element_by_id('exp-ul')
    exp_time = exp_el.find_elements_by_class_name('cbp_tmtime')
    exp_labels = exp_el.find_elements_by_class_name('cbp_tmlabel')
    for j in range(0, len(exp_time)):
        print(exp_time[j].text +": "+exp_labels[j].text)

#list of education qualification
if len(driver.find_elements_by_id('qua-ul')) > 0:
    edu_el = driver.find_element_by_id('qua-ul')
    edu_time = edu_el.find_elements_by_class_name('cbp_tmtime')
    edu_labels = edu_el.find_elements_by_class_name('cbp_tmlabel')
    for j in range(0, len(exp_time)):
        print(edu_time[j].text +": "+edu_labels[j].text)

#list of all patents              
inf = driver.find_elements_by_id('pt-form-view')
if len(inf) > 0:
    boxes = inf[0].find_elements_by_class_name('tag-box')
    if len(boxes) > 0:
        for box in boxes:
            print(box.text)

#scrape projects
proj_el = driver.find_elements_by_id('rp-form-view')
if len(proj_el) > 0:
    projects = proj_el[0].find_elements_by_class_name('tag-box')
    if len(projects) > 0:
        for project in projects:
            print(project.text)


# print(citations)
# print(personal_link)
driver.quit()