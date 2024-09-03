import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir las coordenadas de los vértices del cubo
vertices = [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
           [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]]

# Definir las aristas del cubo
aristas = [(0, 1), (1, 2), (2, 3), (3, 0),
          (4, 5), (5, 6), (6, 7), (7, 4),
          (0, 4), (1, 5), (2, 6), (3, 7)]

# Crear una figura y un subplot 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar las aristas del cubo
for arista in aristas:
    x = [vertices[arista[0]][0], vertices[arista[1]][0]]
    y = [vertices[arista[0]][1], vertices[arista[1]][1]]
    z = [vertices[arista[0]][2], vertices[arista[1]][2]]
    ax.plot(x, y, z, color='black')

# Agregar etiquetas a los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar la figura
plt.show()