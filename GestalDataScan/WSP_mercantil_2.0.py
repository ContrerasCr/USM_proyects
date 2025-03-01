from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


score = 934

wb1 = openpyxl.load_workbook('BBDD Empresas Arreglada.xlsx')
core = wb1['Datos']

def get_data(i):
    razon_social = driver.find_element_by_class_name("separador_mobile").text
    razon = razon_social.split('\n')

    try:
        razon = razon[1]
        print(razon)
    except (IndexError, ValueError):
        print('razon social error')

    rut = driver.find_element_by_id('tatyid').text
    rut_text = rut.split('\n')
    try:
        rut = rut_text[1]
        print(rut)
    except IndexError:
        print('rut error')
    local = driver.find_element_by_xpath("//span[@itemprop='addressLocality']").text
    print(local)

    try:
        core['A' + str(i)] = razon
    except ValueError:
        pass

    try:
        core['B' + str(i)] = rut
    except ValueError:
        pass

    try:
        core['D' + str(i)] = local
    except ValueError:
        pass

    wb1.save('BBDD Empresas Arreglada.xlsx')
    driver.close()


##### -----------------------------------------



len_core = len(core['A']) + 1

row = ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(score, len_core):
    value = str(core['A' + str(i)].value)

    val = [str(core['A' + str(i)].value), str(core['B' + str(i)].value), str(core['D' + str(i)].value)]

    if val[0] != 'None' and val[1] != 'None' and val[2] != 'None':
        continue
    else:
        print(val[0], val[1], val[2], 'fill', 'A' + str(i))
        base_url = "https://www.mercantil.com"
        search_term = str(value)
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)  # 10 is in seconds
        driver.maximize_window()
        driver.get(base_url)
        assert "mercantil" in driver.title
        searchTextBox = driver.find_element_by_css_selector("input[placeholder='Actividad, Empresa, Rut, Dirección']")
        searchTextBox.clear()
        searchTextBox.send_keys(search_term)
        searchTextBox.send_keys(Keys.RETURN)

        src = driver.page_source

        if re.search(r'No pudimos encontrar nada que coincidiera con tu', src):
            driver.close()
            print('listo if')
            continue
        else:

            try:
                searchTextBox_value = driver.find_element_by_id('compLink')
                link_value = searchTextBox_value.get_attribute('href')
                driver.get(link_value)
                get_data(i)
            except NoSuchElementException:
                try:
                    razon_social = driver.find_element_by_class_name("separador_mobile").text
                    get_data(i)
                except NoSuchElementException:
                    print("No link")
                    driver.close()

print('End')
