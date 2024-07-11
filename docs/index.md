##  Bienvenido a Heat Project Documentation

Esta pagina contiene el proyecto de documentación para la función que resuelve la ecuación de calor: ftcs_calor.

##Tabla de Contenidos

1. [Guía de Uso](reference.md)

## Vista del Proyecto


::: heat


## Método Diferencias Finitas:

Este método consiste en la discretización espacial y temporal del dominio para la aproximación de las derivadas parciales de los distintos nodos en la maya. Lo anterior permite transformar el problema de ecuaciones parciales a un sistema de ecuaciones que se pueda resolver de forma numérica.

Para la discretización espacial del problema se debe tomar en cuenta que al ser bidimensional se debe dividir en una maya bidimensional $\ [0,L_x] x [0,L_y] $. Se definen todos los nodos en los ejes x y y de manera que $\ x_i = i \delta x $ donde $\ \Delta x = \frac{L_x}{N_x} $ y de forma análoga $\ y_n = n \Delta y $ donde $\ \Delta y = \frac{L_y}{N_y} $. Para la discretización temporal se tiene un intervalo de tiempo $\ [0 , T] $ que se divide en M subdivisiones y definimos el salto temporal como $\ h = \frac{T}{M} $.

Una vez discretizado el dominio, se procede a la aproximar las derivadas parciales para estas ser evaluadas en un tiempo t. La idea es crear un sistema numérico explícito con el que poder calcular la temperatura que tendrá un punto en la grilla después de que pase un tiempo h a partir de la temperatura de los cuatro nodos vecinos. Aproximando las derivadas y evaluandolas en el tiempo se obtiene la expresión:

$$
\\u_{i,j}^{n+1} = u_{i,j}^{n} + \alpha \frac{\Delta t}{\Delta x^2} (u_{i+1,j}^{n} - 2u_{i,j}^{n} + u_{i-1,j}^{n}) + \alpha \frac{\Delta t}{\Delta y^2} (u_{i,j+1}^{n} - 2u_{i,j}^{n} + u_{i,j-1}^{n})
$$


