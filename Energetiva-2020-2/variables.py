import numpy as np


def dat_nut():
    datos_nutricionales = np.array([['Plátano', 95.03, 1.06, 20.80, 7.30, 0.59, 0.04, 11.50],
                                   ['Zanahoria', 23.91, 0.63, 4.75, 27.00, 0.50, 0.44, 3.80],
                                   ['Berenjena', 21.02, 1.25, 2.39, 16.39, 0.40, 0.01, 5.87],
                                   ['Espinaca', 20.74, 2.63, 0.61, 117.00, 2.70, 0.59, 40.00],
                                   ['Repollo', 30.20, 1.38, 4.18, 45.00, 0.41, 0.01, 48.00],
                                   ['Lechuga', 19.60, 1.37, 1.40, 34.70, 1.00, 0.19, 13.00],
                                   ['Cebolla', 31.85, 1.19, 5.30, 25.40, 0.27, 0.00, 6.90],
                                   ['Pimiento verde', 19.68, 0.63, 1.60, 11.31, 0.49, 0.03, 107.19],
                                   ['Pimiento rojo', 32.90, 1.25, 4.20, 11.89, 0.37, 0.54, 138.73],
                                   ['Zapallo cocido', 32.00, 1.10, 7.70, 18.30, 0.40, 0.74, 6.50],
                                   ['Tomate', 22.17, 0.88, 3.50, 10.60, 0.70, 0.22, 26.60],
                                   ['Palta', 233.0, 1.88, 0.40, 12.00, 0.49, 0.01, 6.00],
                                   ['Naranja', 45.48, 0.87, 8.90, 41.00, 0.49, 0.03, 50.60],
                                   ['Lima', 8.00, 0.60, 1.00, 24.00, 0.00, 0.00, 42.00],
                                   ['Limón', 27.66, 0.69, 3.16, 11.00, 0.45, 0.06, 0.04],
                                   ['Guayaba', 57.00, 0.82, 11.90, 17.00, 0.60, 0.07, 273.00],
                                   ['Mango', 61.13, 0.63, 12.80, 12.00, 0.40, 0.21, 37.00],
                                   ['Piña', 50.76, 0.44, 10.40, 14.50, 0.41, 0.01, 14.99],
                                   ['Sandía', 28.40, 0.63, 5.60, 6.72, 0.29, 0.04, 6.34],
                                   ['Papa cocida', 73.59, 2.34, 14.80, 6.40, 0.43, 0.09, 17.00],
                                   ['Apio', 19.20, 1.19, 2.47, 41.00, 0.40, 0.01, 7.00],
                                   ['Coliflor cocida', 27.52, 2.44, 0.00, 19.26, 0.84, 0.01, 58.77],
                                   ['Haba cocida', 50.40, 5.40, 4.20, 23.00, 1.80, 0.01, 24.00],
                                   ['Cereza', 72.50, 0.88, 13.30, 17.00, 0.35, 0.01, 15.00],
                                   ['Damasco', 41.68, 0.88, 8.54, 16.00, 0.65, 0.28, 6.00],
                                   ['Manzana', 54.08, 0.31, 11.40, 5.50, 0.56, 0.00, 12.40],
                                   ['Nuez', 649.00, 14.42, 4.40, 87.10, 2.80, 0.00, 2.60],
                                   ['Almendra', 589.00, 19.13, 6.20, 248.25, 3.59, 0.00, 0.00],
                                   ['Kiwi', 51.80, 1.00, 9.12, 34.11, 0.37, 0.01, 43.14]])

    return datos_nutricionales


def consumo_agua():
    cons_agua = np.array([['Plátano', 378],
                         ['Zanahoria', 92],
                         ['Berenjena', 129],
                         ['Espinaca', 112],
                         ['Repollo', 80],
                         ['Lechuga', 52],
                         ['Cebolla', 139],
                         ['Pimiento verde', 48],
                         ['Pimiento rojo', 48],
                         ['Zapallo cocido', 96],
                         ['Tomate', 72],
                         ['Palta', 156],
                         ['Naranja', 175],
                         ['Lima', 140],
                         ['Limón', 140],
                         ['Guayaba', 168],
                         ['Mango', 215],
                         ['Piña', 348],
                         ['Sandía', 242],
                         ['Papa', 100],
                         ['Apio', 158],
                         ['Coliflor cocida', 117],
                         ['Haba cocida', 238],
                         ['Cereza', 198],
                         ['Damasco', 106],
                         ['Manzana', 280],
                         ['Nuez', 201],
                         ['Almendra', 226],
                         ['Kiwi', 130]])
    return cons_agua


def dat_dic_nut():
    datos_nutricionales = {'Plátano': [95.03, 1.06, 20.80, 7.30, 0.59, 0.04, 11.50],
                           'Zanahoria': [23.91, 0.63, 4.75, 27.00, 0.50, 0.44, 3.80],
                           'Berenjena': [21.02, 1.25, 2.39, 16.39, 0.40, 0.01, 5.87],
                           'Espinaca': [20.74, 2.63, 0.61, 117.00, 2.70, 0.59, 40.00],
                           'Repollo': [30.20, 1.38, 4.18, 45.00, 0.41, 0.01, 48.00],
                           'Lechuga': [19.60, 1.37, 1.40, 34.70, 1.00, 0.19, 13.00],
                           'Cebolla': [31.85, 1.19, 5.30, 25.40, 0.27, 0.00, 6.90],
                           'Pimiento verde': [19.68, 0.63, 1.60, 11.31, 0.49, 0.03, 107.19],
                           'Pimiento rojo': [32.90, 1.25, 4.20, 11.89, 0.37, 0.54, 138.73],
                           'Zapallo cocido': [32.00, 1.10, 7.70, 18.30, 0.40, 0.74, 6.50],
                           'Tomate': [22.17, 0.88, 3.50, 10.60, 0.70, 0.22, 26.60],
                           'Palta': [233.0, 1.88, 0.40, 12.00, 0.49, 0.01, 6.00],
                           'Naranja': [45.48, 0.87, 8.90, 41.00, 0.49, 0.03, 50.60],
                           'Lima': [8.00, 0.60, 1.00, 24.00, 0.00, 0.00, 42.00],
                           'Limón': [27.66, 0.69, 3.16, 11.00, 0.45, 0.06, 0.04],
                           'Guayaba': [57.00, 0.82, 11.90, 17.00, 0.60, 0.07, 273.00],
                           'Mango': [61.13, 0.63, 12.80, 12.00, 0.40, 0.21, 37.00],
                           'Piña': [50.76, 0.44, 10.40, 14.50, 0.41, 0.01, 14.99],
                           'Sandía': [28.40, 0.63, 5.60, 6.72, 0.29, 0.04, 6.34],
                           'Papa cocida': [73.59, 2.34, 14.80, 6.40, 0.43, 0.09, 17.00],
                           'Apio': [19.20, 1.19, 2.47, 41.00, 0.40, 0.01, 7.00],
                           'Coliflor cocida': [27.52, 2.44, 0.00, 19.26, 0.84, 0.01, 58.77],
                           'Haba cocida': [50.40, 5.40, 4.20, 23.00, 1.80, 0.01, 24.00],
                           'Cereza': [72.50, 0.88, 13.30, 17.00, 0.35, 0.01, 15.00],
                           'Damasco': [41.68, 0.88, 8.54, 16.00, 0.65, 0.28, 6.00],
                           'Manzana': [54.08, 0.31, 11.40, 5.50, 0.56, 0.00, 12.40],
                           'Nuez': [649.00, 14.42, 4.40, 87.10, 2.80, 0.00, 2.60],
                           'Almendra': [589.00, 19.13, 6.20, 248.25, 3.59, 0.00, 0.00],
                           'Kiwi': [51.80, 1.00, 9.12, 34.11, 0.37, 0.01, 43.14]}

    return datos_nutricionales


def consumo_dict_agua():
    cons_agua = {'Plátano': 378,
                 'Zanahoria': 92,
                 'Berenjena': 129,
                 'Espinaca': 112,
                 'Repollo': 80,
                 'Lechuga': 52,
                 'Cebolla': 139,
                 'Pimiento verde': 48,
                 'Pimiento rojo': 48,
                 'Zapallo cocido': 96,
                 'Tomate': 72,
                 'Palta': 156,
                 'Naranja': 175,
                 'Lima': 140,
                 'Limón': 140,
                 'Guayaba': 168,
                 'Mango': 215,
                 'Piña': 348,
                 'Sandía': 242,
                 'Papa cocida': 100,
                 'Apio': 158,
                 'Coliflor cocida': 117,
                 'Haba cocida': 238,
                 'Cereza': 198,
                 'Damasco': 106,
                 'Manzana': 280,
                 'Nuez': 201,
                 'Almendra': 226,
                 'Kiwi': 130}
    return cons_agua


def lista_alimentos():
    cons_agua = ['Plátano',
                 'Zanahoria',
                 'Berenjena',
                 'Espinaca',
                 'Repollo',
                 'Lechuga',
                 'Cebolla',
                 'Pimiento verde',
                 'Pimiento rojo',
                 'Zapallo cocido',
                 'Tomate',
                 'Palta',
                 'Naranja',
                 'Lima',
                 'Limón',
                 'Guayaba',
                 'Mango',
                 'Piña',
                 'Sandía',
                 'Papa',
                 'Apio',
                 'Coliflor cocida',
                 'Haba cocida',
                 'Cereza',
                 'Damasco',
                 'Manzana',
                 'Nuez',
                 'Almendra',
                 'Kiwi']
    return cons_agua

"""var_Plátano
        var_Zanahoria
        var_Berenjena
        var_Espinaca
        var_Repollo
        var_Lechuga
        var_Cebolla
        var_Pimiento verde
        var_Pimiento rojo
        var_Zapallo cocido
        var_Tomate
        var_Palta
        var_Naranja
        var_Lima
        var_Limón
        var_Guayaba
        var_Mango
        var_Piña
        var_Sandía
        var_Papa
        var_Apio
        var_Coliflor cocida
        var_Haba cocida
        var_Cereza
        var_Damasco
        var_Manzana
        var_Nuez
        var_Almendra
        var_Kiwi """

'''var_platano = IntVar(value=0)
var_zanahoria = IntVar(value=0)
var_berenjena = IntVar(value=0)
var_espinaca = IntVar(value=0)
var_repollo = IntVar(value=0)
var_lechuga = IntVar(value=0)
var_cebolla = IntVar(value=0)
var_pimiento_verde = IntVar(value=0)
var_pimiento_rojo = IntVar(value=0)
var_zapallo_cocido = IntVar(value=0)
var_tomate = IntVar(value=0)
var_palta = IntVar(value=0)
var_naranja = IntVar(value=0)
var_lima = IntVar(value=0)
var_limon = IntVar(value=0)
var_guayaba = IntVar(value=0)
var_mango = IntVar(value=0)
var_pina = IntVar(value=0)
var_papa = IntVar(value=0)
var_apio = IntVar(value=0)
var_coliflor_cocida = IntVar(value=0)
var_haba_cocida = IntVar(value=0)
var_cereza = IntVar(value=0)
var_damasco = IntVar(value=0)
var_manzana = IntVar(value=0)
var_nuez = IntVar(value=0)
var_almendra = IntVar(value=0)
var_kiwi = IntVar(value=0)'''


'''        self.v_pla = [95.03, 1.06, 20.80, 7.30, 0.59, 0.04, 11.50]
        self.v_zan = [23.91, 0.63, 4.75, 27.00, 0.50, 0.44, 3.80]
        self.v_ber = [21.02, 1.25, 2.39, 16.39, 0.40, 0.01, 5.87]
        self.v_esp = [20.74, 2.63, 0.61, 117.00, 2.70, 0.59, 40.00]
        self.v_rep = [30.20, 1.38, 4.18, 45.00, 0.41, 0.01, 48.00]
        self.v_lec = [19.60, 1.37, 1.40, 34.70, 1.00, 0.19, 13.00]
        self.v_ceb = [31.85, 1.19, 5.30, 25.40, 0.27, 0.00, 6.90]
        self.v_pve = [19.68, 0.63, 1.60, 11.31, 0.49, 0.03, 107.19]
        self.v_pro = [32.90, 1.25, 4.20, 11.89, 0.37, 0.54, 138.73]
        self.v_zco = [32.00, 1.10, 7.70, 18.30, 0.40, 0.74, 6.50]
        self.v_tom = [22.17, 0.88, 3.50, 10.60, 0.70, 0.22, 26.60]
        self.v_pal = [233.0, 1.88, 0.40, 12.00, 0.49, 0.01, 6.00]
        self.v_nar = [45.48, 0.87, 8.90, 41.00, 0.49, 0.03, 50.60]
        self.v_lima = [8.00, 0.60, 1.00, 24.00, 0.00, 0.00, 42.00]
        self.v_lim = [27.66, 0.69, 3.16, 11.00, 0.45, 0.06, 0.04]
        self.v_gua = [57.00, 0.82, 11.90, 17.00, 0.60, 0.07, 273.00]
        self.v_man = [61.13, 0.63, 12.80, 12.00, 0.40, 0.21, 37.00]
        self.v_pin = [50.76, 0.44, 10.40, 14.50, 0.41, 0.01, 14.99]
        self.v_san = [28.40, 0.63, 5.60, 6.72, 0.29, 0.04, 6.34]
        self.v_pap = [73.59, 2.34, 14.80, 6.40, 0.43, 0.09, 17.00]
        self.v_api = [19.20, 1.19, 2.47, 41.00, 0.40, 0.01, 7.00]
        self.v_cco = [27.52, 2.44, 0.00, 19.26, 0.84, 0.01, 58.77]
        self.v_hab = [50.40, 5.40, 4.20, 23.00, 1.80, 0.01, 24.00]
        self.v_cer = [72.50, 0.88, 13.30, 17.00, 0.35, 0.01, 15.00]
        self.v_dam = [41.68, 0.88, 8.54, 16.00, 0.65, 0.28, 6.00]
        self.v_man = [54.08, 0.31, 11.40, 5.50, 0.56, 0.00, 12.40]
        self.v_nue = [649.00, 14.42, 4.40, 87.10, 2.80, 0.00, 2.60]
        self.v_alm = [589.00, 19.13, 6.20, 248.25, 3.59, 0.00, 0.00]
        self.v_kiw = [51.80, 1.00, 9.12, 34.11, 0.37, 0.01, 43.14]'''


'''        self.v_pla = 
        self.v_zan = 
        self.v_ber = 
        self.v_esp = 
        self.v_rep = 
        self.v_lec = 
        self.v_ceb = 
        self.v_pve = 
        self.v_pro = 
        self.v_zco = 
        self.v_tom = 
        self.v_pal = 
        self.v_nar = 
        self.v_lima = 
        self.v_lim = 
        self.v_gua = 
        self.v_man = 
        self.v_pin = 
        self.v_san = 
        self.v_pap = 
        self.v_api = 
        self.v_cco = 
        self.v_hab = 
        self.v_cer = 
        self.v_dam = 
        self.v_man =
        self.v_nue = 
        self.v_alm = 
        self.v_kiw = '''