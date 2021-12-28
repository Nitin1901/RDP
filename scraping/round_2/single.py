from selenium import webdriver
import time

driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://pu.irins.org/profile/59252")

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
links = []

if len(ids) > 0:
    for id in ids:
        id_link = id.find_element_by_tag_name('a').get_attribute('href')
        # print(id_link)
        txt = id.text.split('\n')
        professor_id = {
            "name":txt[0],
            "ID": txt[1],
            "link": id_link
        }
        links.append(professor_id)
        


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
        interest = interest_el[0].text.split(', ')
research = {
    "area": area,
    "interests": interest
}

#personal info
if len(driver.find_elements_by_id('list_panel_personal')) > 0:
    personal_info = driver.find_element_by_id('list_panel_personal')
    link_el = personal_info.find_elements_by_tag_name('a')
    if len(link_el) > 0:
        personal_link = link_el[0].get_attribute('href')
    
#list of experience
experience_list = []
if len(driver.find_elements_by_id('exp-ul')) > 0:
    exp_el = driver.find_element_by_id('exp-ul')
    exp_time = exp_el.find_elements_by_class_name('cbp_tmtime')
    exp_labels = exp_el.find_elements_by_class_name('cbp_tmlabel')
    for j in range(0, len(exp_time)):
        exp_split = exp_labels[j].text.split('\n')
        exp = {
            "duration": exp_time[j].text,
            "designation": exp_split[0],
            "department": exp_split[1],
            "university": exp_split[2]
        }
        experience_list.append(exp)

#list of education qualification
qualification_list = []
if len(driver.find_elements_by_id('qua-ul')) > 0:
    edu_el = driver.find_element_by_id('qua-ul')
    edu_time = edu_el.find_elements_by_class_name('cbp_tmtime')
    edu_labels = edu_el.find_elements_by_class_name('cbp_tmlabel')
    for j in range(0, len(edu_time)):
        edu_split = edu_labels[j].text.split('\n')
        qual = {
            "duration": edu_time[j].text,
            "degree": edu_split[0],
            "university": edu_split[1]
        }
        qualification_list.append(qual)
        # print(edu_time[j].text +": "+edu_labels[j].text)

#list of all patents
patents_list = []            
inf = driver.find_elements_by_id('pt-form-view')
if len(inf) > 0:
    boxes = inf[0].find_elements_by_class_name('tag-box')
    if len(boxes) > 0:
        for box in boxes:
            pat_no = box.find_elements_by_tag_name('li')
            box_split = box.text.split('\n')
            if len(box_split) > 1:
                pat = {
                    "name": box_split[0],
                    "authors": box_split[1],
                    "patent_number": pat_no[0].text
                }
                patents_list.append(pat)
            # print(len(box_split))

#scrape projects
proj_el = driver.find_elements_by_id('rp-form-view')
if len(proj_el) > 0:
    projects = proj_el[0].find_elements_by_class_name('tag-box')
    if len(projects) > 0:
        for project in projects:
            print(project.text)


# print(citations)
# print(personal_link)

print("Links")
print(links)
print("\nResearch")
print(research)
print("\nPersonal link")
print(personal_link)
print("\nExperience list")
print(experience_list)
print("\nqualification")
print(qualification_list)
print("\nPatents")
print(patents_list)

driver.quit()