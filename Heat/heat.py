#Heat_Equation/heat.py

import numpy as np

def ftcs_calor(Th, Tc, kappa, L, a, M, N, h, t_fin):

    """
    Método para resolver la ecuación de calor de manera numérica mediante diferencias finitas.

    Examples:
        >>> import numpy as np
        >>> T, its, shape = ftcs_calor(300.0, 20.0, 98.8e-6, 0.3, 0.3, 50, 50, 1e-2, 60.0)
        >>> print(its)
        6001


    Args:
        Th (float): Temperatura alta
        Tc (float): Temperatura baja
        kappa (float): Conductividad Térmica
        L (float): Largo de la placa
        a (float): Ancho de la placa
        M (int): Particiones a lo largo de la placa
        N (int): Particiones a lo ancho de la placa
        h (float): Particiones temporales
        t_fin (float): Tiempo final


    Returns:
        T (array): Matriz de temperaturas a lo largo y ancho de la placa en un tiempo final
        its (int): iteraciones realizadas hasta el tiempo final
        shape (array): Guarda los distintos arreglos de la matriz T a lo largo del tiempo.
    """


    # Condiciones iniciales
    T = np.full((M+1, N+1), Tc, dtype=float)
    T[24:27, 24:27] = Th

    #Los otros parametros
    t = 0.0
    dy= a / (N - 1)  #Particiones del ancho
    dx = L / (M - 1)  #Partciones del largo

    #Para la animacion
    its = 0
    tsteps = int(t_fin / h)
    shape = np.zeros((tsteps + 2, M+1, N+1), dtype=float)

    #Aqui se implementa el FTCS
    while t < t_fin:
        #arreglo para hacer las operaciones con FTCS
        Tk = T.copy()
        for i in range(0, M):
            for j in range(0, N):
               if i < 24 or i > 26 or j < 24 or j > 26:
                    Tk[i, j] = (((kappa*h)/(dy*dx)) * ((dy/dx) * (T[i-1, j] + T[i+1, j] - 2*T[i, j])) + ((kappa*h)/(dy*dx)) * ((dx/dy) * (T[i, j+1] + T[i, j-1] - 2*T[i, j])) + T[i, j])

        T = Tk.copy()
        t += h
        its += 1
        shape[its] = T.copy()
    return T, its, shape
