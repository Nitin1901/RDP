from selenium import webdriver
d = webdriver.Chrome (executable_path="C:\\Program Files (x86)\\chromedriver.exe")
d.maximize_window()
d.get('http://scholar.google.co.in/citations?user=6M4uVi0AAAAJ')
cit_el = d.find_elements_by_id('gsc_rsb_st')
if len(cit_el) > 0:
    citations_el = d.find_element_by_id('gsc_rsb_st')
    rows = citations_el.find_elements_by_tag_name('tr')
    if len(rows) > 0:
        for row in rows:
            print(row.text)