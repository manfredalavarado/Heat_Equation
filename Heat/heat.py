#Heat_Equation/heat.py

import numpy as np

def ftcs_calor(Tp, Tc, Lx, Ly, N, alpha, dt, t):

    """
    Método para resolver la ecuación de calor de manera numérica mediante diferencias finitas.

    Examples:
        >>> import numpy as np
        >>> Tc = 300 # en ºC
        >>> Tp = 20  # en ºC
        >>> Lx = 0.3 # en m
        >>> Ly = 0.3 # en m
        >>> N = 100
        >>> alpha = 98.8e-6 # en m^2/s
        >>> dt = 1e-2
        >>> t = 60
        
        >>> valores, iteraciones, shape = ftcs_calor(Tp, Tc, Lx, Ly, N, alpha, dt, t)
        >>> print(iteraciones)
        601

    Args:
        Tp (float): Temperatura alta
        Tc (float): Temperatura baja
        Lx (float): Largo de la placa
        Ly (float): Ancho de la placa
        N (int): Número de particiones de los lados de la placa
        alpha (float): Conductividad Térmica
        dt (float): Particiones temporales
        t (float): Tiempo final


    Returns:
        T (array): Matriz de temperaturas a lo largo y ancho de la placa en un tiempo final
        its (int): iteraciones realizadas hasta el tiempo final
        shape (array): Guarda los distintos arreglos de la matriz T a lo largo del tiempo.
    """

    #Para centrar la condición inicial
    Pc_i = int(N * 0.5) - 1 # Inicio del punto caliente a la izquierda
    Pc_d = int(N * 0.5) + 1 # Final del punto caliente a la derecha
    Pc_u = int(N * 0.5) - 1 # Inicio del punto caliente arriba
    Pc_d = int(N * 0.5) + 1 # Final del punto caliente abajo

    # Definición de las condiciones iniciales
    u = np.full((N+1, N+1), Tp, dtype=float)
    u[ Pc_i : Pc_d + 1, Pc_u : Pc_d +1] = Tc

    # Otros parametros
    t0 = 0.0             # Tiempo inicial
    dy= Ly / (N - 1)   # Particiones del ancho
    dx = Lx / (N - 1)  # Partciones del largo

    its = 0

    #Para la animación
    tsteps = int(t/dt)
    shape = np.zeros((tsteps + 2, Nx+1, Ny+1), dtype=float)

    #Aqui se implementa el FTCS
    while t0 < t:
        #arreglo para hacer las operaciones con FTCS
        u_c = u.copy()
        for i in range(0, N):
            for j in range(0, N):
               if i < Pc_i or i > Pc_d or j < Pc_u or j > Pc_d:
                    u_c[i, j] = (u[i, j] +
                               alpha * dt / dx**2 * (u[i+1, j] - 2*u[i, j] + u[i-1, j]) +
                               alpha * dt / dy**2 * (u[i, j+1] - 2*u[i, j] + u[i, j-1]))

        u = u_c.copy()
        t0 += dt
        its += 1
        shape[its] = u.copy()
    return T, its, shape
