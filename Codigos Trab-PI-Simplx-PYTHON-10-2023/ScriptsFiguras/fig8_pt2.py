import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('C:\\Users\\Mediconchip\\Downloads\\Codigos-Trabalho PI-Simplx-01-2024\\Codigos-Trabalho PI-Simplx-01-2024\\PI_SIMPLEX_PYTHON\\Codigos Trab-PI-Simplx-PYTHON-10-2023\\ResultsPI\\StepStudiesHibrido.csv'
                 ,delimiter=';', header=0)

passoZero5=df[df["alfa"]==0.05]
passo01=df[df["alfa"]==0.1]
passo03=df[df["alfa"]==0.3]
passo05=df[df["alfa"]==0.5]
passo07=df[df["alfa"]==0.7]
passo08=df[df["alfa"]==0.8]
passo09=df[df["alfa"]==0.9]
passo095=df[df["alfa"]==0.95]
passo099=df[df["alfa"]==0.99]



import matplotlib.pyplot as plt
import numpy as np



# Criar uma figura
plt.figure(figsize=(10, 6))

# Plotar os dados na mesma figura com bolotas e legenda
plt.plot(passoZero5["dim"],passoZero5["Tempo"], 'o-', label='passo=0.05', color='r')    # 'o-' para bolotas com linha
plt.plot(passo01["dim"], passo01["Tempo"], 's-', label='passo=0.1', color='g')  # 's-' para quadrados com linha
plt.plot(passo03["dim"], passo03["Tempo"], '^-', label='passo=0.3', color='b') # '^- para triângulos com linha
plt.plot(passo05["dim"], passo05["Tempo"], '.-', label='passo=0.5', color='c') # '^- para triângulos com linha
plt.plot(passo07["dim"], passo07["Tempo"], 'p-', label='passo=0.7', color='m') # '^- para triângulos com linha
plt.plot(passo08["dim"], passo08["Tempo"], '*-', label='passo=0.8', color='y') # '^- para triângulos com linha
plt.plot(passo09["dim"], passo09["Tempo"], 'H-', label='passo=0.9', color='k') # '^- para triângulos com linha
plt.plot(passo095["dim"], passo095["Tempo"], 'D-', label='passo=0.95', color='r') # '^- para triângulos com linha
plt.plot(passo099["dim"], passo099["Tempo"], '1-', label='passo=0.99', color='g') # '^- para triângulos com linha

# Adicionar título e rótulos aos eixos
plt.title('Avaliação do Passo - Híbrido -Tempo vs Dimensão')
plt.xlabel('Dimensão')
plt.ylabel('Tempo[s]')

# Adicionar uma grade
plt.grid(True)

# Adicionar uma legenda
plt.legend()

# Mostrar o gráfico
plt.show()