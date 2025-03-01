from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


score = 520

wb1 = openpyxl.load_workbook('BBDD Empresas Arreglada.xlsx')
core = wb1['Datos']

def get_data(i):


    razon = driver.find_element_by_xpath("//span[@itemprop='legaName']").text

    rut = driver.find_element_by_xpath("//span[@itemprop='taxID']").text

    rubro = driver.find_element_by_link_text("Actividades Económicas o Giros").text

    local = driver.find_element_by_link_text("Comuna").text

    try:
        core['A' + str(i)] = razon
    except ValueError:
        pass

    try:
        core['B' + str(i)] = rut
    except ValueError:
        pass

    try:
        core['C' + str(i)] = rubro
    except ValueError:
        pass

    try:
        core['D' + str(i)] = local
    except ValueError:
        pass

    #wb1.save('BBDD Empresas Arreglada.xlsx')
    driver.close()


##### -----------------------------------------



len_core = len(core['A']) + 1

row = ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(score, len_core):
    value = str(core['A' + str(i)].value)

    val = [str(core['A' + str(i)].value), str(core['B' + str(i)].value),str(core['C' + str(i)].value), str(core['D' + str(i)].value)]

    if val[0] != 'None' and val[1] != 'None' and val[2] != 'None' and val[3] != 'None':
        continue
    else:
        print(val[0], val[1], val[2], 'fill')
        base_url = "https://www.genealog.cl"
        search_term = str(value)
        #options = Options()
        #options.headless = True
        #driver = webdriver.Chrome(options=options)
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)  # 10 is in seconds
        driver.get(base_url)
        searchTextBox = driver.find_element_by_id('s')
        searchTextBox.send_keys('Aristia')
        searchTextBox.send_keys(Keys.RETURN)


        # Person Type

        #check_personas = driver.find_element_by_xpath("//input[@mytype='personas']").is_selected()
        #check_empresas = driver.find_element_by_xpath("//input[@mytype='empresas']").is_selected()
        #check_lugares = driver.find_element_by_xpath("//input[@mytype='lugares']").is_selected()


        # Pais type

        #check_chile = driver.find_element_by_xpath("//input[@mytype='chile']").is_selected()
        #check_argentina = driver.find_element_by_xpath("//input[@mytype='argentina']").is_selected()
        #check_bolivia = driver.find_element_by_xpath("//input[@mytype='bolivia']").is_selected()
        #check_colombia = driver.find_element_by_xpath("//input[@mytype='colombia']").is_selected()
        #check_guatemala = driver.find_element_by_xpath("//input[@mytype='guatemala']").is_selected()
        #check_mexico = driver.find_element_by_xpath("//input[@mytype='mexico']").is_selected()
        #check_venezuela = driver.find_element_by_xpath("//input[@mytype='venezuela']").is_selected()


        #if check_personas:
        driver.find_element_by_xpath("//span[text()='Personas']").click()

        #if not check_empresas:
        #driver.find_element_by_xpath("//span[text()='Empresas']").click()

        #if check_lugares:
        driver.find_element_by_xpath("//span[text()='Lugares']").click()



        #if not check_chile:
        #driver.find_element_by_xpath("//span[text()='Chile']").click()

        #if check_argentina:
        #driver.find_element_by_xpath("//span[text()='Argentina']").click()

        #if check_bolivia:
        driver.find_element_by_xpath("//span[text()='Bolivia']").click()

        #if check_colombia:
        driver.find_element_by_xpath("//span[text()='Colombia']").click()

        #if check_guatemala:
        driver.find_element_by_xpath("//span[text()='Guatemala']").click()

        #if check_mexico:
        driver.find_element_by_xpath("//span[text()='Mexico']").click()

        #if check_venezuela:
        #driver.find_element_by_xpath("//span[text()='Venezuela']").click()


        try:
            link_empresa = driver.find_element_by_partial_link_text('https://www.genealog.cl/Geneanexus/empresa/CHILE/').get_attribute('href')
            print(link_empresa)
            driver.get(link_empresa)
            pass


        except NoSuchElementException:

            not_find = driver.find_element_by_class_name('noResults')
            print('no results')
            input()
            continue


        input()



print('End')