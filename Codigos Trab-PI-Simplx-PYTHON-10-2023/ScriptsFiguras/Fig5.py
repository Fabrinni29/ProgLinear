import matplotlib.pyplot as plt

# Dados de exemplo
x = [2,4,6,10,14,18,20,22,24,26]
simplex = [0.002059459686279297,
0.003057241439819336,
0.0045964717864990234,
0.07498621940612793,
1.0113909244537354,
96.99655628204346,
448.4811990261078,
2089.004803419113,
533.7346091270447,
2654.9375343322754,
]
PtsIT = [0.005012989044189453,
0.0158846378326416,
0.008997917175292969,
0.006001949310302734,
0.010017871856689453,
0.01730203628540039,
0.015504598617553711,
0.11690878868103027,
0.015999555587768555,
0.8374333928708395,
]
Hybrid = [0.06987524032592773,
0.005999326705932617,
0.023306608200073242,
0.06416058540344238,
0.22323083877563477,
0.10460948944091797,
0.04538249969482422,
0.02544498443603515,
0.027836322784423828,
0.13466739654541016,
]

# Criar uma figura e três subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

# Primeiro subplot
ax1.plot(x, simplex, 'r')
ax1.set_title('Simplex - Tempo de Execução vs Dimensão')
ax1.set_ylabel('Tempo [s]')

# Segundo subplot
ax2.plot(x, PtsIT, 'g')
ax2.set_title('Pontos Interiores')
ax2.set_ylabel('Tempo [s]')

# Terceiro subplot
ax3.plot(x, Hybrid, 'b')
ax3.set_title('Hibrido')
ax3.set_ylabel('Tempo [s]')
ax3.set_xlabel('ndim [n]')

# Ajustar o layout para evitar sobreposição
plt.tight_layout()

# Mostrar os gráficos
plt.show()
