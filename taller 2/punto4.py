from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Crear el problema
problem = LpProblem("Maximizar_Ganancias", LpMaximize)

# Definir las variables
x_p1 = LpVariable("x_p1", lowBound=0, cat="Integer")
x_p2 = LpVariable("x_p2", lowBound=0, cat="Integer")
x_p3 = LpVariable("x_p3", lowBound=0, cat="Integer")
x_g1 = LpVariable("x_g1", lowBound=0, cat="Integer")
x_g2 = LpVariable("x_g2", lowBound=0, cat="Integer")
x_g3 = LpVariable("x_g3", lowBound=0, cat="Integer")
x_a1 = LpVariable("x_a1", lowBound=0, cat="Integer")
x_a2 = LpVariable("x_a2", lowBound=0, cat="Integer")
x_a3 = LpVariable("x_a3", lowBound=0, cat="Integer")

# Definir la función objetivo
problem += 50 * (x_p1 + x_p2 + x_p3) + 30 * (x_g1 + x_g2 + x_g3) + 60 * (x_a1 + x_a2 + x_a3)

# Restricciones de capacidad
problem += 5 * x_p1 + 25 * x_g1 + 31 * x_a1 >= 10000
problem += 5 * x_p2 + 25 * x_g2 + 31 * x_a2 >= 12000
problem += 5 * x_p3 + 25 * x_g3 + 31 * x_a3 >= 9000

# Restricciones de espacio
problem += 30 * x_p1 + 20 * x_g1 + 8 * x_a1 <= 4800
problem += 30 * x_p2 + 20 * x_g2 + 8 * x_a2 <= 5760
problem += 30 * x_p3 + 20 * x_g3 + 8 * x_a3 <= 4320

# Restricciones de presupuesto
problem += 7800 * x_p1 + 23500 * x_g1 + 13730 * x_a1 <= 5000000
problem += 7800 * x_p2 + 23500 * x_g2 + 13730 * x_a2 <= 6000000
problem += 7800 * x_p3 + 23500 * x_g3 + 13730 * x_a3 <= 4500000

# Resolver el problema
problem.solve()

# Imprimir los resultados
print(f"Paneles Solares Zona 1: {x_p1.varValue}")
print(f"Paneles Solares Zona 2: {x_p2.varValue}")
print(f"Paneles Solares Zona 3: {x_p3.varValue}")
print(f"Generadores Eólicos Zona 1: {x_g1.varValue}")
print(f"Generadores Eólicos Zona 2: {x_g2.varValue}")
print(f"Generadores Eólicos Zona 3: {x_g3.varValue}")
print(f"Generadores Gasolina Zona 1: {x_a1.varValue}")
print(f"Generadores Gasolina Zona 2: {x_a2.varValue}")
print(f"Generadores Gasolina Zona 3: {x_a3.varValue}")
print(f"Ganancia Total: {problem.objective.value()}")
