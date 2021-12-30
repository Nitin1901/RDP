from selenium import webdriver
import time

driver = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://vidwan.inflibnet.ac.in/searchc/search")

researchers = []
professor_links = []

def google_scholar_scrape(link):
    citations = dict()
    link = link.replace('http://', 'https://')
    d = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
    d.maximize_window()
    d.get(link)
    cit_el = d.find_elements_by_id('gsc_rsb_st')
    if len(cit_el) > 0:
        citations_el = d.find_element_by_id('gsc_rsb_st')
        rows = citations_el.find_elements_by_tag_name('tr')
        if len(rows) > 0:
            for row in rows:
                if 'Citations' in row.text:
                    citations["count"] = row.text.split(' ')[1]
                if 'h-index' in row.text:
                    citations["h_index"] = row.text.split(' ')[1]
    
    d.quit()
    print(citations)
    return citations
    

if len(driver.find_elements_by_class_name('list-product-description')) > 0:
    rows = driver.find_elements_by_class_name('list-product-description')
    for row in rows:
        info = row.text.split('\n')
        id = info[0][info[0].index(': '):]
        name = info[1]
        designation = info[2]
        university = info[-2]
        dept = None
        link_el = row.find_element_by_class_name('col-sm-3')
        link = link_el.find_element_by_tag_name('a').get_attribute('href')
        professor_links.append(link)
        area = info[3]
        interests = info[4].split(',')
        image = row.find_element_by_tag_name('img')
        image = image.get_attribute('src')
        row = {
            "id": id,
            "name": name,
            "affiliations": {
                "designation": designation,
                "university": university,
                "department": dept
            },
            "education": None,
            "profile_link": None,
            "profile_picture": image,
            # "website": None,
            # "research": {
            #     "area": area,
            #     "interests": interests
            # },
            "research_area": area,
            "research_interests": interests,
            "citations": None,
            "h_index": None,
            "experience": None,
            "publications": None,
            "patents": None,
            "projects": None,
            "academic_identity": None,
            "similar_experts": None
        }
        researchers.append(row)

for link,researcher in zip(professor_links,researchers):
    driver.get(link)

    # Academic identity links and IDs
    research_id_count = driver.find_elements_by_id('identity-view')
    if len(research_id_count) > 0:
        research_id_el = driver.find_element_by_id('identity-view')
        ids = research_id_el.find_elements_by_class_name('notification')
        academic_identity = []
        values = dict()
        if len(ids) > 0:
            for id in ids:
                id_link = id.find_element_by_tag_name('a').get_attribute('href')
                # print(id_link)
                txt = id.text.split('\n')
                researcher_id = {
                    "name":txt[0],
                    "ID": txt[1],
                    "link": id_link
                }
                if('Google Scholar' in txt[0]):
                    values = google_scholar_scrape(id_link)
                    print(values)
                academic_identity.append(researcher_id)

            researcher["citations"] = values["count"] if "count" in values else None
            researcher["h_index"] = values["h_index"] if "h_index" in values else None
            researcher["academic_identity"] = academic_identity
        # print(researcher["citations"])

    #personal info
    if len(driver.find_elements_by_id('list_panel_personal')) > 0:
        personal_info = driver.find_element_by_id('list_panel_personal')
        link_el = personal_info.find_elements_by_tag_name('a')
        if len(link_el) > 0:
            personal_link = link_el[0].get_attribute('href')
            researcher["profile_link"] = personal_link

    #list of experience
    experience_list = []
    if len(driver.find_elements_by_id('exp-ul')) > 0:
        exp_el = driver.find_element_by_id('exp-ul')
        exp_time = exp_el.find_elements_by_class_name('cbp_tmtime')
        exp_labels = exp_el.find_elements_by_class_name('cbp_tmlabel')
        for j in range(0, len(exp_time)):
            exp_split = exp_labels[j].text.split('\n')
            if len(exp_split) > 2:
                exp = {
                    "duration": exp_time[j].text,
                    "designation": exp_split[0],
                    "department": exp_split[1],
                    "university": exp_split[2]
                }
                if(j == 0):
                    researcher["affiliations"]["department"] = exp_split[1]
            else:
                exp = {
                    "duration": exp_time[j].text,
                    "designation": exp_split[0],
                    "department": None,
                    "university": exp_split[1]
                }
            experience_list.append(exp)
        researcher["experience"] = experience_list

    #list of education qualification
    qualification_list = []
    if len(driver.find_elements_by_id('qua-ul')) > 0:
        edu_el = driver.find_element_by_id('qua-ul')
        edu_time = edu_el.find_elements_by_class_name('cbp_tmtime')
        edu_labels = edu_el.find_elements_by_class_name('cbp_tmlabel')
        for j in range(0, len(edu_time)):
            edu_split = edu_labels[j].text.split('\n')
            if len(edu_split) > 1:
                qual = {
                    "duration": edu_time[j].text,
                    "degree": edu_split[0],
                    "university": edu_split[1]
                }
            else:
                qual = {
                    "duration": edu_time[j].text,
                    "degree": edu_split[0],
                    "university": None
                }
            qualification_list.append(qual)
        researcher["education"] = qualification_list

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
            researcher["patents"] = patents_list
    
    #list of all projects
    projects_list = []
    proj_el = driver.find_elements_by_id('rp-form-view')
    if len(proj_el) > 0:
        projects = proj_el[0].find_elements_by_class_name('tag-box')
        if len(projects) > 0:
            for project in projects:
                if project.text != '':
                    proj_split = project.text.split('\n')
                    if len(proj_split) > 1:
                        project_detail = {
                            "name": proj_split[0],
                            "details": proj_split[1:]
                        }
                    else:
                        project_detail = {
                            "name": proj_split[0]
                        }
                    projects_list.append(project_detail)
            researcher["projects"] = projects_list
    
    #list of similar experts
    similar_experts = []
    experts_cnt = driver.find_elements_by_id('list_expert')
    if len(experts_cnt) > 0:
        experts_el = driver.find_element_by_id('list_expert')
        experts_li = experts_el.find_elements_by_tag_name('a')
        experts_names = experts_el.find_elements_by_tag_name('strong')
        for j in range (0, len(experts_li)):
            l = experts_li[j].get_attribute('href')
            exp = {
                "name": experts_names[j].text,
                "ID": l[l.index('profile/')+8:]
            }
            similar_experts.append(exp)
    researcher["similar_experts"] = similar_experts

    publications_list = []
    sidenav = driver.find_elements_by_class_name('list-group-item')
    if len(sidenav) > 0:
        for item in sidenav:
            # print(item.text)
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
                            volume = None
                            year = None
                            title = publication.find_element_by_tag_name('h2')
                            authors = publication.find_element_by_tag_name('p')
                            elements = publication.find_element_by_class_name('label-info')
                            type = elements.text
                            remaining_text = publication.text
                            remaining_text = remaining_text.replace(title.text, "")
                            remaining_text = remaining_text.replace(authors.text, "")
                            remaining_text = remaining_text.replace(type, "")
                            remaining_text = remaining_text.split("\n")
                            for i in remaining_text:
                                if i:
                                    l = i.split(",")
                                    l = [i.strip().lower() for i in l]
                                    journal = l[0]
                                    for j in l[1:]:
                                        x = j.split(' ')
                                        if x[0].lower() == 'volume' and len(x)>1:
                                            volume = x[1]
                                        elif x[0].lower() == 'year' and len(x)>1:
                                            year = x[1]
                                    break
                            publication_item = {
                                "title": title.text,
                                "authors": authors.text.split(';'),
                                "type": type,
                                "journal": journal,
                                "volumn": volume,
                                "year": year
                            }
                            publications_list.append(publication_item)
                        researcher["publications"] = publications_list

    # print(researcher)

print(researchers)
driver.quit()

# Code to push all the data to database
# from pymongo import MongoClient

# client = MongoClient("mongodb+srv://rdp:ETXTQD0ARke4vPqU@cluster0.ttc9e.mongodb.net/RDP?retryWrites=true&w=majority")
# db = client["RDP"]
# collection = db["Researchers"]
# result = collection.insert_many(researchers)
# print(result)