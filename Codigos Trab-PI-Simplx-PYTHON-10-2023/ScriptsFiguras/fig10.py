import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('C:\\Users\\Mediconchip\\Downloads\\Codigos-Trabalho PI-Simplx-01-2024\\Codigos-Trabalho PI-Simplx-01-2024\\PI_SIMPLEX_PYTHON\\Codigos Trab-PI-Simplx-PYTHON-10-2023\\ResultsPI\\DualGapHibrido.csv'
                 ,delimiter=';', header=0)

menos1=df[df["GAP"]==0.1]
menos2=df[df["GAP"]==0.01]
menos4=df[df["GAP"]==0.0001]
menos6=df[df["GAP"]==1e-06]
menos8=df[df["GAP"]==1e-08]
menos10=df[df["GAP"]==1e-10]




import matplotlib.pyplot as plt



# Criar uma figura
plt.figure(figsize=(10, 6))

# Plotar os dados na mesma figura com bolotas e legenda
plt.plot(menos1["dim"],menos1["Iters"], 'o-', label='GAP=0.1', color='r')    # 'o-' para bolotas com linha
plt.plot(menos2["dim"], menos2["Iters"], 's-', label='GAP=0.01', color='g')  # 's-' para quadrados com linha
plt.plot(menos4["dim"], menos4["Iters"], '^-', label='GAP=0.0001', color='b') # '^- para triângulos com linha
plt.plot(menos6["dim"], menos6["Iters"], '.-', label='GAP=1e-06', color='c') # '^- para triângulos com linha
plt.plot(menos8["dim"], menos8["Iters"], 'p-', label='GAP=1e-08', color='m') # '^- para triângulos com linha
plt.plot(menos10["dim"], menos10["Iters"], '*-', label='GAP=1e-10', color='y') # '^- para triângulos com linha

# Adicionar título e rótulos aos eixos
plt.title('Gap de Dualidade- Híbrido - Iterações vs Dimensão')
plt.xlabel('Dimensão')
plt.ylabel('Iterações')

# Adicionar uma grade
plt.grid(True)

# Adicionar uma legenda
plt.legend()

# Mostrar o gráfico
plt.show()