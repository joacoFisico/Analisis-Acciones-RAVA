# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 09:01:21 2016

@author: joaquin
"""

'''
Distintas funciones de visualización de datos
'''

import matplotlib.pyplot as plt
import scipy.signal as sig
import numpy
import matplotlib.pyplot as plt

def ajusteCuadratico(datos_crudos, graficar = False):
    maximo = max(datos_crudos)
    cant_datos = len(datos_crudos)
    datos_normalizados = [0]*cant_datos
    for n in xrange(cant_datos):
        datos_normalizados[n] = datos_crudos[n]/maximo
        
    datos_savgol = sig.savgol_filter(datos_normalizados, 5, 1)
    
    fit_datos = numpy.polyfit(range(cant_datos), datos_savgol, 2)
    polinomio = numpy.poly1d(fit_datos)
    datos_poly = polinomio(range(cant_datos))
    
    if graficar:
        plt.plot(datos_savgol)
        plt.plot(datos_poly)
        plt.show()
    
    return datos_poly, fit_datos