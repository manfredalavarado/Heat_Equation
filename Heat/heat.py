#Heat_Equation/heat.py

import numpy as np

def ftcs_calor(Tp, Tc, Lx, Ly, Nx, Ny, alpha, dt, t):

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

    #Para centrar la condición inicial
    Pc_i = int(Nx * 0.5) - 1 # Inicio del punto caliente a la izquierda
    Pc_d = int(Nx * 0.5) + 1 # Final del punto caliente a la derecha
    Pc_u = int(Nx * 0.5) - 1 # Inicio del punto caliente arriba
    Pc_d = int(Nx * 0.5) + 1 # Final del punto caliente abajo

    # Definición de las condiciones iniciales
    u = np.full((Nx+1, Ny+1), Tp, dtype=float)
    u[ Pc_i : Pc_d + 1, Pc_u : Pc_d +1] = Tc

    # Otros parametros
    t0 = 0.0             # Tiempo inicial
    dy= Ly / (Ny - 1)   # Particiones del ancho
    dx = Lx / (Nx - 1)  # Partciones del largo

    its = 0

    #Para la animación
    tsteps = int(t/dt)
    shape = np.zeros((tsteps + 2, Nx+1, Ny+1), dtype=float)

    #Aqui se implementa el FTCS
    while t0 < t:
        #arreglo para hacer las operaciones con FTCS
        u_c = u.copy()
        for i in range(0, Nx):
            for j in range(0, Ny):
               if i < Pc_i or i > Pc_d or j < Pc_u or j > Pc_d:
                    u_c[i, j] = (u[i, j] +
                               alpha * dt / dx**2 * (u[i+1, j] - 2*u[i, j] + u[i-1, j]) +
                               alpha * dt / dy**2 * (u[i, j+1] - 2*u[i, j] + u[i, j-1]))

        u = u_c.copy()
        t += dt
        its += 1
        shape[its] = u.copy()
    return T, its, shape
