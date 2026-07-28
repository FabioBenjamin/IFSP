import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import product

# Cria a figura
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

# Vértices do cubo externo
outer = list(product([-1, 1], repeat=3))

# Vértices do cubo interno (menor)
scale = 0.5
inner = [(x * scale, y * scale, z * scale) for x, y, z in outer]

# Função para desenhar um cubo
def desenhar_cubo(vertices):
    for i, v1 in enumerate(vertices):
        for j, v2 in enumerate(vertices):
            # Liga apenas vértices que diferem em uma coordenada
            if sum(a != b for a, b in zip(v1, v2)) == 1:
                ax.plot(
                    [v1[0], v2[0]],
                    [v1[1], v2[1]],
                    [v1[2], v2[2]],
                    color="blue",
                    linewidth=2
                )

# Desenha os dois cubos
desenhar_cubo(outer)
desenhar_cubo(inner)

# Liga os vértices correspondentes
for o, i in zip(outer, inner):
    ax.plot(
        [o[0], i[0]],
        [o[1], i[1]],
        [o[2], i[2]],
        color="",
        linewidth=2
    )

# Remove eixos, números e grade
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_axis_off()

# Fundo branco
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

# Mantém a proporção correta
ax.set_box_aspect([1, 1, 1])

plt.show()