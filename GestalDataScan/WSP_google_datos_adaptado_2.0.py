from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options


score = 2271

wb1 = openpyxl.load_workbook('BBDD Empresas Arreglada.xlsx')
core = wb1['Datos']


def get_data_mercantil(celda):

    datos = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', celda]

    razon_social = driver.find_element_by_xpath('//span[@itemprop="name"]').text

    rut = driver.find_element_by_id('tatyid').text
    rut_text = rut.split('\n')
    try:
        rut = rut_text[1]
    except IndexError:
        print('rut error')
    direccion = driver.find_element_by_xpath("//span[@itemprop='addressLocality']").text

    datos[0] = razon_social
    datos[1] = rut
    datos[3] = direccion

    return datos


def get_data_genealog(celda):

    datos = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', celda]

    try:
        driver.find_element_by_id('nuevaVersionMessage').click()

    except NoSuchElementException:
        pass

    razon_social = driver.find_element_by_xpath("//td[@itemprop='legalName']").text
    rut = driver.find_element_by_xpath("//td[@itemprop='taxID']").text
    rubro = driver.find_element_by_class_name("maxHeight200").text
    area = rubro.split('\n')
    rubro = area[-1]
    direccion = driver.find_element_by_xpath('//*[@id="results-content"]/tr[8]/td[2]').text
    datos[0] = razon_social
    datos[1] = rut
    datos[2] = rubro
    datos[3] = direccion

    return datos


def get_data_mercado_publico(celda):

    datos = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', celda]

    razon_social = driver.find_element_by_id('lblSocialReasonDesc').text
    rut = driver.find_element_by_id('lblRutDesc').text
    direccion = driver.find_element_by_id('lblAddressDesc').text
    contacto = driver.find_element_by_id('lblContactDesc').text
    mail = driver.find_element_by_id('lblMailDesc').text
    fono = driver.find_element_by_id('lblphoneDesc').text

    datos[0] = razon_social
    datos[1] = rut
    datos[3] = direccion
    datos[4] = contacto
    datos[5] = mail
    datos[6] = fono

    return datos


def get_data_svs(celda):

    datos = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', celda]

    valores = driver.find_element_by_id('contenido').text
    contenido = valores.split('\n')

    for data in contenido:
        if ('RUT' in data) and ('-' in data):
            rut = data.split(' ', 1)
            datos[1] = rut[-1]

        if 'Razón Social' in data and (len(data.split(' ')) >= 3):
            razon_social = data.split(' ')
            razon_social.remove('Razón')
            razon_social.remove('Social')
            datos_new = ' '.join(razon_social)
            datos[0] = datos_new

        if 'Teléfono' in data and (len(data.split(' ')) >= 2):
            telefono = data.split(' ', 1)
            datos[6] = (telefono[1])

        if 'Comuna' in data and (len(data.split(' ')) >= 2):
            comuna = data.split(' ', 1)
            datos[3] = comuna[1]

        if 'e-mail' in data and (len(data.split(' ')) >= 4):
            email = data.split(' ')
            email_new = email[-1]
            datos[5] = email_new

    return datos


def get_data_webportal_mercado_publico(celda):

    datos = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', celda]

    razon_social = driver.find_element_by_id('lblRazonSocial').text
    rut = driver.find_element_by_id('lblRut').text

    try:
        rubro = driver.find_element_by_id('lblGiro').text
        datos[2] = rubro
    except NoSuchElementException:
        pass

    try:
        direccion = driver.find_element_by_id('lblAddressDesc').text
        datos[3] = direccion
    except NoSuchElementException:
        pass

    try:
        contacto = driver.find_element_by_id('lblPersonaContacto').text
        datos[4] = contacto
    except NoSuchElementException:
        pass

    try:
        mail = driver.find_element_by_id('lblMail').text
        datos[5] = mail
    except NoSuchElementException:
        pass

    try:
        fono = driver.find_element_by_id('lblTelefonoContacto').text
        datos[6] = fono
    except NoSuchElementException:
        pass

    datos[0] = razon_social
    datos[1] = rut

    return datos


def save_bbdd(razon_social, rut, rubro, direccion, contacto, mail, fono, celda):

    try:
        core['A' + str(celda)] = razon_social
    except ValueError:
        print('Error', 'A', celda)
        pass

    try:
        core['B' + str(celda)] = rut
    except ValueError:
        print('Error', 'B', celda)
        pass

    try:
        core['C' + str(celda)] = rubro
    except ValueError:
        print('Error', 'C', celda)
        pass

    try:
        core['D' + str(celda)] = direccion
    except ValueError:
        print('Error', 'D', celda)
        pass

    values = [core['A' + str(celda)].value, core['B' + str(celda)].value, core['C' + str(celda)].value,
              core['D' + str(celda)].value, core['E' + str(celda)].value, core['F' + str(celda)].value,
              core['G' + str(celda)].value]

    print(values)
    wb1.save('BBDD Empresas Arreglada.xlsx')


def del_webcache(lista):

    links = lista
    for vale in lista:

        if 'webcache' in vale:
            posicion = lista.index(vale)
            links.pop(posicion)
    return links


def del_webportal(lista):

    link_wo_webportal = []
    for kal in lista:
        if 'webportal' not in kal:
            link_wo_webportal.append(kal)

    return link_wo_webportal


def get_webportal(lista):

    link_wo_webportal = []
    for kal in lista:
        if 'webportal' in kal:
            link_wo_webportal.append(kal)

    return link_wo_webportal


def clean_svs(lista):

    link_wo_webportal = []
    for kal in lista:
        if 'www.svs.cl' in kal:
            link_wo_webportal.append(kal)

    return link_wo_webportal


def val_faltantes(i):

    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    faltantes = [False, False, False, False, False, False, False]

    for vale in columns:
        pos = columns.index(vale)
        if core[vale+str(i)] != 'None':
            faltantes[pos] = True

    return faltantes


def minusculas(lista):

    nueva = []
    for i in range(len(lista)-1):

        palabra = lista[i].lower()
        nueva.append(palabra)
    return nueva


def completar_faltante(mercantil_dat, mercadopublico_dat, webportal_dat, genealog_dat, svs_dat, celda):

    datos = ['None', 'None', 'None', 'None', 'None', 'None', 'None', celda]

    mercantil_min = minusculas(mercantil_dat)
    mercadopublico_min = minusculas(mercadopublico_dat)
    webportal_min = minusculas(webportal_dat)
    genealog_min = minusculas(genealog_dat)
    svs_min = minusculas(svs_dat)

#    print(mercantil_min[0], mercadopublico_min[0], webportal_min[0], genealog_min[0], svs_min[0], 'razon social')

    dat = [mercantil_min, mercadopublico_min, webportal_min, genealog_min, svs_min]
    reales = [mercantil_min, mercadopublico_min, webportal_min, genealog_min, svs_min]

    for i in dat:
        if i[0] == 'None':
            reales.remove(i)
    if len(reales) == 0:
        return False
    razon = reales[0][0]
    datos[0] = solve_razonsocial(reales[0][0])

    for j in range(len(reales)):
        if datos[0] == solve_razonsocial(reales[j][0]):
            for k in range(len(reales[j])):
                if datos[k] == 'None' and reales[j][k] != 'none':
                    datos[k] = reales[j][k]

#    print(datos, 'finales')
#    save_bbdd(razon, datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7])


def solve_razonsocial(name):

    if '.' in name:
        newname = list(name)

        while '.' in newname:
            newname.remove('.')

        brandname = ''.join(newname)
        return brandname

    else:
        return name


def get_datos (search_term):


    driver.get(base_url)
    searchTextBox = driver.find_element_by_name('q')
    searchTextBox.clear()
    searchTextBox.send_keys(search_term)
    searchTextBox.send_keys(Keys.RETURN)
    src = driver.page_source
    if re.search(r'No se han encontrado resultados para tu', src):
        driver.close()
        print('no se encontraron resultados', score)
        pass
    else:

        try:
            recharge = driver.find_element_by_id('taw')
            recharge.click()
        except ElementClickInterceptedException:
            pass

        searchTextBox_value = driver.find_elements_by_class_name('rc [href]')

        genealog = []
        mercantil = []
        svs = []
        mercado_publico = []

        for link in searchTextBox_value:

            link_individual = link.get_attribute('href')
            driver.implicitly_wait(2)

            if 'genealog' in str(link_individual):
                genealog.append(link_individual)
            if 'mercantil' in str(link_individual):
                mercantil.append(link_individual)
            if 'svs' in str(link_individual):
                svs.append(link_individual)
            if 'mercadopublico' in str(link_individual):
                mercado_publico.append(link_individual)

            

        genealog = del_webcache(genealog)
        mercantil = del_webcache(mercantil)
        svs = del_webcache(svs)
        svs = clean_svs(svs)
        mercado_publico = del_webcache(mercado_publico)
        mercado_publico = del_webportal(mercado_publico)
        web_portal = get_webportal(mercado_publico)

        datos_mercantil = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
        datos_mercado_publico = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
        datos_webportal = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
        datos_genealog = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
        datos_svs = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']

        existencia = [mercantil, mercado_publico, web_portal, genealog, svs]


        try:
            driver.get(mercantil[0])
            datos_mercantil = get_data_mercantil(coor)

        except (IndexError, NoSuchElementException):
            pass

        try:
            driver.get(web_portal[0])
            datos_webportal = get_data_webportal_mercado_publico(coor)

        except (IndexError, NoSuchElementException):
            pass

        try:
            driver.get(mercado_publico[0])
            datos_mercado_publico = get_data_mercado_publico(coor)

        except (IndexError, NoSuchElementException):
            pass

        try:
            driver.get(genealog[0])
            datos_genealog = get_data_genealog(coor)

        except (IndexError, NoSuchElementException):
            pass

        try:
            driver.get(svs[0])
            datos_svs = get_data_svs(coor)

        except (IndexError, NoSuchElementException):
            pass

        datos = [datos_mercantil, datos_webportal, datos_mercado_publico, datos_genealog, datos_svs]

        dat = [datos, existencia]

        return dat





# -----------  Fin Funciones  ------------------------------


len_core = len(core['A']) + 1

row = ['A', 'B', 'C', 'D', 'E', 'F']
for coor in range(score, len_core):
    try:

        for coor in range(score, len_core):
            value = str(core['A' + str(coor)].value)

            val = [str(core['A' + str(coor)].value), str(core['B' + str(coor)].value),
                   str(core['C' + str(coor)].value), str(core['D' + str(coor)].value)]

            if val[0] != 'None' and val[1] != 'None' and val[2] != 'None' and val[3] != 'None':
                continue

            else:
                print(val[0], val[1], val[2], val[3], 'fill', 'A' + str(coor), 'iniciales')
                base_url = "https://www.google.cl"
                search_term = str(value) + ' rut datos empresa'
                options = Options()
                options.headless = True
                driver = webdriver.Chrome(options=options)
    #            driver = webdriver.Chrome()

                datos = get_datos(search_term)

                valores = datos[1]
                validar = datos[0]

                if len(validar[0]) == 0 and len(validar[0]) == 0 and len(validar[0]) == 0 and len(validar[0]) == 0 and len(validar[0]) == 0 :
                    datos = get_datos(str(value) + ' rut datos empresa')

                valores = datos[1]

                datos_mercantil = valores[0]
                datos_mercado_publico = valores[1]
                datos_webportal = valores[2]
                datos_genealog = valores[3]
                datos_svs = valores[4]

                driver.close()
                completar_faltante(datos_mercantil, datos_mercado_publico,
                                       datos_webportal, datos_genealog, datos_svs, coor)

    except TimeoutException:
        pass

print('End')
