# -*- coding: utf-8 -*-
"""Copia de Examen del primer parcial.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Zy0r8CXuOvwSH3PAUkmdddVCat5UdFBI
"""

import numpy as np
import matplotlib.pyplot as plt

# Importante: verifica que tu nombre y número de matrícula esten correctos
nombre = "César Alejandro Cerrillo Domínguez"
numero_de_matricula = 179289
fecha = '2025-02-26'

"""1.   El 30 de junio de 1992, la capitalización de mercados de valores del Pacífico y Asia fue:

País |  Capitalización (en miles de millones de dólares)
-----|---------------------------------------------------
Filipinas | 17
Indonesia | 21
Tailandia | 44
Singapur | 50
Malasia | 79
Corea del Sur | 86
Taiwan | 140
Hong Kong | 178
Australia | 203

* a) Encuentre la media aritmética de los datos
* b) Encuentre la mediana de los datos
* c) Encuentre la desviación estándar de los datos

regrese una tupla en el siguiente orden:
(media, mediana, desv_est)
"""

datos = pd.DataFrame({'Capitalizacion': [17,21,44,50,79,86,140,178,203]})

def capitalizacion():
    media = datos['Capitalizacion'].mean()
    mediana = datos['Capitalizacion'].median()
    desv_est = np.std(datos['Capitalizacion'])
    return (media, mediana, desv_est)

"""2.    La aistencia a los 10 últimos partidos en casa de las Águilas de Baltimore fue la siguiente:



20100, 24500, 31600, 28400, 49500, 19350, 25600, 30600, 11300, 28560


Calcule el rango, la varianza y la desviación stándard para estos datos

Regrese una tupla con el siguiente orden:

(rango, varianza, desv_est)
"""

partidos = pd.DataFrame({'Partidos': [20100,24500,31600,28400,49500,19350,25600,30600,11300,28560]})
def asistencia_dispersion():
    rango = partidos['Partidos'].max() - partidos['Partidos'].min()
    varianza = np.var(partidos['Partidos'])
    desv_est = np.std(partidos['Partidos'])
    return (rango, varianza, desv_est)

"""3.    Genere un histograma de las siguientes calificaciones en el examen parcial:

7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2, 6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2, 9.3, 10.0, 8.9

Nota: regrese el histograma generado con la función de numpy con 10 bins, no genere la gráfica
"""

data = pd.DataFrame({'Cali': [7.9, 7.8, 7.8, 6.7, 7.6, 8.7, 8.5, 7.3, 6.6, 9.9, 8.4, 7.2, 6.6, 5.7, 9.4, 8.4, 7.2, 6.3, 5.1, 4.8, 5.0, 6.1, 7.1, 8.2, 9.3, 10.0, 8.9]})
def histograma_np():
    return plt.hist(data, bins=5)

"""4.    Analiza la correlación entre los datos de Tamaño y Precio y

Regresa el coeficiente de Pearson


   Tamaño (m²) | Precio (MXN)
   ------------|------------
          100  |    1305710
          120  |    1658277
          140  |    1894167
          160  |    2136552
          180  |    2298267
          200  |    2553624
          220  |    2780503
          240  |    3289726
          260  |    3472743
          280  |    3779477
"""

def correlacion():
    x = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280])
    y = np.array([1305710, 1658277, 1894167, 2136552, 2298267,2553624,2780503,3289726,3472743,3779477])

    mean_x = np.mean(x)
    mean_y = np.mean(y)

    deviation_x = x - mean_x
    deviation_y = y - mean_y

    product_deviations = deviation_x * deviation_y

    sum_product_deviations = np.sum(product_deviations)

    std_x = np.std(x, ddof=1)
    std_y = np.std(y, ddof=1)

    r = sum_product_deviations / ((len(x) - 1) * std_x * std_y)
    return r

"""5.        La tienda de departamentso Friendly ha sido objeto de muchos robos durante el último mes; pero debido al aumento a las medidas de seguridad, se han detenido 250 ladrones. Se registró el sexo de cada ladrón; también se anotó si se trataba de un primer delito o era reincidente. Los datos se resumen en la siguiente tabla.

Sexo | Primera ofensa | Reincidente
-----|----------------|------------
Hombre | 60 | 70
Mujer | 44 | 76

Suponga que se selecciona al azar un ladrón detenido, calcule
* la probabilidad de que el ladrón sea hombre: p_hombre
* la probabilidad de que sea la primera ofensa, dado que es hombre: p_po_hombre

Regrese ambos datos en una tupla con el siguiente orden
(p_hombre, p_po_hombre)
"""

def calcular_probabilidades():
    hombres_primera_ofensa = 60
    hombres_reincidente = 70
    mujeres_primera_ofensa = 44
    mujeres_reincidente = 76

    total_ladrones = hombres_primera_ofensa + hombres_reincidente + mujeres_primera_ofensa + mujeres_reincidente

    p_hombre = (hombres_primera_ofensa + hombres_reincidente) / total_ladrones

    p_po_hombre = hombres_primera_ofensa / (hombres_primera_ofensa + hombres_reincidente)

    return (p_hombre, p_po_hombre)

"""Contesta las siguientes preguntas

Definición del Problema:

6.     ¿Cuál es el problema específico que se desea resolver con la minería de datos?
7.     ¿Por qué es importante resolver este problema?

Objetivos del Proyecto:

8.     ¿Cuáles son los objetivos principales del anteproyecto?
9.     ¿Qué resultados esperas obtener al final del proyecto?

Recolección de Datos:

10.    ¿Qué tipo de datos se necesitarán para este proyecto?

Regresa cadenas de texto con tu respuesta.
"""

def problema_especifico():
    return """
    El problema especifico es cuando se requiere predecir valores futuros no conocibles, a prtir de un gran conjunto de datos
    """

def importancia():
    return """
    Permite tomar desiciones correctas y basadas en datos, para tener un mejor control de las acciones que se desean realizar
    """

def objetivos():
    return """
    Descubrir posibles datos futuros, haciendo previsaulizaciones de datos futuros
    """

def tipo_de_datos():
    return """
    Comportamiento, transaccionales, demográficos etc
    """
