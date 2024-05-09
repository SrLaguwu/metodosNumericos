import numpy as np

# Definir los valores iniciales y los parámetros
N0 = 100  # Concentración inicial de bacterias
r = 0.1  # Tasa de crecimiento intrínseca de bacterias
Nmax = 1000  # Concentración máxima de bacterias
dt = 0.008333  # Intervalo de tiempo (30 segundos = 0.008333 horas)
t_final = 10  # Tiempo final (10 horas)

# Crear una lista para almacenar los valores de concentración de bacterias
tiempos = np.arange(0, t_final + dt, dt)
concentraciones = np.zeros_like(tiempos)
concentraciones[0] = N0  # Valor inicial

# Aplicar el método de Euler
for i in range(1, len(tiempos)):
    N = concentraciones[i - 1]
    dN_dt = r * N * (1 - N / Nmax)
    concentraciones[i] = N + dN_dt * dt

# Imprimir los resultados
for t, N in zip(tiempos, concentraciones):
    print(f"Tiempo: {t:.2f} horas, Concentración de bacterias: {N:.2f} unidades")