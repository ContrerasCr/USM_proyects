from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl
import re
from selenium.common.exceptions import NoSuchElementException

option = webdriver.ChromeOptions()




wb1 = openpyxl.load_workbook('BBDD Empresas Arreglada.xlsx')
core = wb1['Datos']
len_core = len(core['A']) + 1

row = ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(2, len_core):
    value = str(core['A' + str(i)].value)

    val = [str(core['A' + str(i)].value),str(core['B' + str(i)].value),str(core['D' + str(i)].value)]

    if val[0] != 'None' and val[1] != 'None' and val[2] != 'None':
        print(val[0], val[1], val[2], 'Complete')
        continue
    else:
        print(val[0], val[1], val[2], 'fill')
        # declare variable to store the URL to be visited
        base_url = "https://www.mercantil.com"
        # declare variable to store search term
        search_term = str(value)
        # -- Pre - Condition --
        # declare and initialize driver variable
        driver = webdriver.Chrome()
        # driver should wait implicitly for a given duration, for the element under consideration to load.
        # to enforce this setting we will use builtin implicitly_wait() function of our 'driver' object.
        driver.implicitly_wait(10) #10 is in seconds
        # to load a given URL in browser window
        driver.get(base_url)
        # test whether correct URL/ Web Site has been loaded or not
        assert "mercantil" in driver.title
        # -- Steps --
        # to enter search term, we need to locate the search textbox
        searchTextBox = driver.find_element_by_css_selector("input[placeholder='Actividad, Empresa, Rut, Dirección']")

        # to clear any text in the search textbox
        searchTextBox.clear()
        # to enter the search term in the search textbox via send_keys() function
        searchTextBox.send_keys(search_term)
        # to search for the entered search term
        searchTextBox.send_keys(Keys.RETURN)
        # to verify if the search results page loaded

        src = driver.page_source

        if re.search(r'No pudimos encontrar nada que coincidiera con tu', src):
            driver.close()
            print('listo if')
            continue
        else:
            print('listo else')



            try :
                searchTextBox_value = driver.find_element_by_id('compLink')
                link_value = searchTextBox_value.get_attribute('href')
                driver.get(link_value)
            except NoSuchElementException:
                print("No link")


            razon_social = driver.find_element_by_class_name("separador_mobile").text
            razon = razon_social.split('\n')
            razon = razon[1]
            print(razon)

            rut = driver.find_element_by_id('tatyid').text
            rut_text = rut.split('\n')
            rut = rut_text[1]
            print(rut)

            local = driver.find_element_by_xpath("//span[@itemprop='addressLocality']").text
            print(local)

            # -- Post - Condition --
            # to close the browser


            core['A' +str(i)] = razon
            core['B' + str(i)] = rut
            core['D' + str(i)] = local

            #wb1.save('BBDD Empresas Arreglada.xlsx')
            driver.close()
            print('listo')


print('End')



#HAcer una funcin del caso en que funciona