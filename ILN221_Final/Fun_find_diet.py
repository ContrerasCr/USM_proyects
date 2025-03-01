import numpy as np
import time


def dieta_optima(max_alimentos, dieta_opt):
    start = time.time()
    # max_alimentos = Cantidad maxima de un alimento que puede comer una persona en un dia [int]
    # dieta_optima = dieta a la cual se va a modelar el problema [lista de 7 valores]
    # Mejores alimentos Nuez, Almendra, Papa cocida, Espinaca, Pimiento Rojo
    max_alimentos = max_alimentos * 10
    array_dieta_optima = np.array(dieta_opt)
    valor_ideal = [0, 2061,  (0, 0, 0, 0, 0)]
    # Valor ideal[0] = Valor que se busca maximizar gradiante
    # Valor ideal[1] = Valor que se busca minimizar agua

    matriz_best_alimentos = np.array([[649.00, 14.42, 4.40, 87.10, 2.80, 0.00, 2.60],
                                      [589.00, 19.13, 6.20, 248.25, 3.59, 0.00, 0.00],
                                      [73.59, 2.34, 14.80, 6.40, 0.43, 0.09, 17.00],
                                      [20.74, 2.63, 0.61, 117.00, 2.70, 0.59, 40.00],
                                      [32.90, 1.25, 4.20, 11.89, 0.37, 0.54, 138.73]])

    matriz_best_al_water = np.array([201, 226, 100, 112, 48])

    all_values = [[a, b, c, d, e] for a in range(max_alimentos) for b in range(max_alimentos)
                  for c in range(max_alimentos) for d in range(max_alimentos) for e in range(max_alimentos)]

    print(time.time()-start)

    for values in all_values:
        vector_cant_alim = np.transpose(np.array([values])/10)
        matriz_total = vector_cant_alim * matriz_best_alimentos
        vector_total = matriz_total.sum(axis=0)
        relacion = vector_total / array_dieta_optima
        gradiante_nut = pow((relacion[0] * relacion[1] * relacion[2] * relacion[3] * relacion[4] * relacion[5] * relacion[6]), (1/10))
        grad_agua = np.dot(vector_cant_alim,    matriz_best_al_water)
        print(grad_agua)
        if (gradiante_nut > valor_ideal[0]) and (grad_agua < valor_ideal[1]):
            valor_ideal = [gradiante_nut, grad_agua, values]
            print(time.time()-start)
        else:
            continue

    print(valor_ideal)
    print(time.time()-start)
    return valor_ideal


dieta_optima(3, [1900, 69, 250, 664, 12, 0.4, 55])

# End document
