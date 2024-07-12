import matplotlib.pyplot as plt

# Dados de exemplo
x = [2,4,6,10,14,18,20,22,24,26]
simplex = [3,
15,
63,
1023,
16383,
262143,
1048575,
4194303,
16777215,
67108863
]
PtsIT = [8,
8,
8,
8,
8,
8,
8,
8,
8,
8
]
Hybrid = [3,
6,
15,
207,
3279,
9,
9,
9,
9,
9
]

# Criar uma figura e três subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

# Primeiro subplot
ax1.plot(x, simplex, 'r')
ax1.set_title('Simplex - Número de Iterações vs Dimensão')
ax1.set_ylabel('Iterações')

# Segundo subplot
ax2.plot(x, PtsIT, 'g')
ax2.set_title('Pontos Interiores')
ax2.set_ylabel('Iterações')

# Terceiro subplot
ax3.plot(x, Hybrid, 'b')
ax3.set_title('Hibrido')
ax3.set_ylabel('Iterações')
ax3.set_xlabel('ndim [n]')

# Ajustar o layout para evitar sobreposição
plt.tight_layout()

# Mostrar os gráficos
plt.show()
