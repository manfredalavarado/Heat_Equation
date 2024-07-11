##  Bienvenido a Heat Project Documentation

Esta pagina contiene el proyecto de documentación para la función que resuelve la ecuación de calor mediante Forward-Time Central-Space (FTCS).

##Tabla de Contenidos

1. [Guía de Uso](reference.md)

## Vista del Proyecto


::: Heat


## Método Diferencias Finitas:

Este método consiste en la discretización espacial y temporal del dominio para la aproximación de las derivadas parciales de los distintos nodos en la maya. Lo anterior permite transformar el problema de ecuaciones parciales a un sistema de ecuaciones que se pueda resolver de forma numérica.

Para la discretización espacial del problema se debe tomar en cuenta que al ser bidimensional se debe dividir en una maya bidimensional $[ 0 , L_{x} ] x  [ 0 , L_{y} ]$. Se definen todos los nodos en los ejes X y Y de manera que $\\x_{i} = i \Delta x$ donde $\Delta x = \frac{L_{x}}{N_{x}}$ y de forma análoga $\\y_{n} = n \Delta y$ donde $\Delta y = \frac{L_{y}}{N_{y}}$. Para la discretización temporal se tiene un intervalo de tiempo $[ 0 , T ]$ que se divide en M subdivisiones y definimos el salto temporal como $h = \frac{T}{M}$.


Una vez discretizado el dominio, se procede a la aproximar las derivadas parciales para estas ser evaluadas en un tiempo t. La idea es crear un sistema numérico explícito con el que poder calcular la temperatura que tendrá un punto en la grilla después de que pase un tiempo h a partir de la temperatura de los cuatro nodos vecinos. Aproximando las derivadas y evaluandolas en el tiempo se obtiene la expresión:

$$
\\u_{i,j}^{n+1} = u_{i,j}^{n} + \alpha \frac{\Delta t}{\Delta x^2} (u_{i+1,j}^{n} - 2u_{i,j}^{n} + u_{i-1,j}^{n}) + \alpha \frac{\Delta t}{\Delta y^2} (u_{i,j+1}^{n} - 2u_{i,j}^{n} + u_{i,j-1}^{n})
$$

El calculo de la ecuación de calor mediante diferencias finitas ofrece ventajas como una mayor flexibilidad, una precisión ajustable y una capacidad para manejar variadas condiciones de frontera lo que le permite adaptarse a distintos tipos de problemas. Además, es un método que ofrece una alta eficiencia computacional, lo que lo hace fácil de implementar en variedad de condiciones.



#Participantes:
- René Bernardo Rivera Brenes (C26461)
- Anaité Chaves Ramírez (C12154)
- Kendall Alvarado Quesada (C20368)
- Joel Ignacio Moreno Calderón (C15292)
- Manfred Alvarado López (C10318)
