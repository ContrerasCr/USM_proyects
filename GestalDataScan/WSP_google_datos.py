from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

from selenium.webdriver.chrome.options import Options


score = 876

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
    datos[3] =direccion

    save_bbdd(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7])
    driver.close()


def get_data_genealog(celda):


    datos = ['None', 'None', 'None', 'None', 'None', 'None', 'None', celda]

    try:
        new_page = driver.find_element_by_id('nuevaVersionMessage').click()

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

    save_bbdd(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7])
    driver.close()



def get_data_mercado_publico(celda):


    datos = ['None', 'None', 'None', 'None', 'None', 'None', 'None', celda]

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

    save_bbdd(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7])

    driver.close()


def get_data_svs(celda):

    datos = ['None','None','None','None','None','None','None','None', celda]

    valores = driver.find_element_by_id('contenido').text
    datos = valores.split('\n')

    for data in datos:
        if ('RUT' in data) and ('-' in data):
            rut = data.split(' ', 1)
            datos[1] = rut


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

        if 'e-mail' in data  and (len(data.split(' ')) >= 4):
            email = data.split(' ')
            email_new = email[-1]
            datos[5] = email_new


    save_bbdd(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7] )
    driver.close()


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


    save_bbdd(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5], datos[6], datos[7])

    driver.close()



def save_bbdd(razon_social, rut, rubro, direccion, contacto, mail, fono, celda):

    try:
        core['A' + str(i)] = razon_social
    except ValueError:
        print('Error', 'A', celda)
        pass

    try:
        core['B' + str(i)] = rut
    except ValueError:
        print('Error', 'B', celda)
        pass

    try:
        core['C' + str(i)] = rubro
    except ValueError:
        print('Error', 'C', celda)
        pass

    try:
        core['D' + str(i)] = direccion
    except ValueError:
        print('Error', 'D', celda)
        pass

    try:
        core['E' + str(i)] = contacto
    except ValueError:
        print('Error', 'E', celda)
        pass

    try:
        core['F' + str(i)] = mail
    except ValueError:
        print('Error', 'F', celda)
        pass

    try:
        core['G' + str(i)] = fono
    except ValueError:
        print('Error', 'G', celda)
        pass


    wb1.save('BBDD Empresas Arreglada.xlsx')

def del_webcache(lista):

    links = lista
    for value in lista:

        if 'webcache' in value:
            posicion = lista.index(value)
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


##### -----------  Fin Funciones  ------------------------------



len_core = len(core['A']) + 1

row = ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(score, len_core):
    value = str(core['A' + str(i)].value)

    val = [str(core['A' + str(i)].value), str(core['B' + str(i)].value), str(core['C' + str(i)].value), str(core['D' + str(i)].value)]

    if val[0] != 'None' and val[1] != 'None' and val[2] != 'None' and val[3] != 'None':
        continue
    else:
        print(val[0], val[1], val[2], 'fill', 'A' + str(i))
        base_url = "https://www.google.cl"
        search_term = str(value) + ' rut datos empresa'
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        #driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get(base_url)
        searchTextBox = driver.find_element_by_name('q')
        searchTextBox.clear()
        searchTextBox.send_keys(search_term)
        searchTextBox.send_keys(Keys.RETURN)

        src = driver.page_source

        if re.search(r'No se han encontrado resultados para tu', src):
            driver.close()
            print('no se encontraron resultados', score)
            continue
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

                prioridad = ['mercado publico', 'genealog', 'mercantil', 'svs']


            genealog = del_webcache(genealog)
            mercantil = del_webcache(mercantil)
            svs = del_webcache(svs)
            mercado_publico = del_webcache(mercado_publico)
            mercado_publico = del_webportal(mercado_publico)
            web_portal = get_webportal(mercado_publico)

            try:
                driver.get(mercantil[0])
                get_data_mercantil(i)
            except (IndexError, NoSuchElementException) as e:
                try:
                    driver.get(web_portal[0])
                    get_data_webportal_mercado_publico(i)

                except (IndexError, NoSuchElementException) as e:

                    try:
                        driver.get(mercado_publico[0])
                        get_data_mercado_publico(i)

                    except (IndexError, NoSuchElementException) as e:

                        try:
                            driver.get(genealog[0])
                            get_data_genealog(i)
                        except (IndexError, NoSuchElementException) as e:
                            #try:
                            #    driver.get(svs[0])
                            #    get_data_svs(i)
                            #except IndexError:
                            print('sin base de datos', i)
                            pass

        if val[0] != 'None' and val[1] != 'None' and val[2] != 'None' and val[3] != 'None' and val[4] != 'None' and val[5] != 'None'  and val[6] != 'None'  and val[7] != 'None':
            pass


print('End')