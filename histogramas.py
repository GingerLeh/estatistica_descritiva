#carregamento das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
# %matplotlib widget

#Geração dos dados
s1 = pd.Series([7, 7, 6, 2,	5, 4, 3, 7,	3, 1, 2, 4, 8, 6, 3, 7, 9, 6, 1, 3]) #gera uma série de dados
pd.DataFrame.head(s1)

s2 = pd.Series([3, 3, 5, 12, 3, 4, 10, 5, 4, 4, 3, 4, 8, 4, 5, 5, 6, 6, 4, 7])
pd.DataFrame.head(s2)

s3 = pd.Series([7, 7, 7, 8, 8, 7, 7, 7, 4, 8, 7, 8, 8, 9, 8, 8, 7, 9, 8, 8])
pd.DataFrame.head(s3)

#Gráfico de histograma

#gráfico único

# Cria uma imagem vazia
fig = plt.figure()

# Plota o histograma
plt.hist(s1, bins = 5) #bins são as barras

# Coloca título nos eixos
plt.title("Distribuição da variável S1", loc = 'left')

# Coloca nome nos eixos
plt.xlabel('s1')
plt.ylabel('Frequência')
plt.show()

#Múltiplos gráficos

# Cria a figura e os subplots
fig = plt.figure()
plt.subplots_adjust(hspace = 0.3, wspace = 0.4) #mais de um gráfico numa mesma imagem
fig.suptitle('Comparação de distribuições', x=0.1, y=.95, horizontalalignment = 'left', verticalalignment = 'top')
ax1 = fig.add_subplot(2, 2, 1) #os números são as coordenadas (2 linhas e 2 colunas e este será o primeiro gráfico)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

# Cria os gráficos de histograma e acerta os nomes dos eixos
ax1.hist(s1, bins = 5) #agora adiciona os dados no gráfico
ax1.set_xlabel('s1')
ax1.set_ylabel('Frequência')

ax2.hist(s2, bins = 5)
ax2.set_xlabel('s2')
ax2.set_ylabel('Frequência')

ax3.hist(s3, bins = 5)
ax3.set_xlabel('s3')
ax3.set_ylabel('Frequência')

#Histogramas superpostos
fig = plt.figure() #3 layers de uma mesmo gráfico
plt.hist(s1, alpha = 0.5, label = 's1')
plt.hist(s2, alpha = 0.5, label = 's1')
plt.hist(s3, alpha = 0.5, label = 's1')
# Código alternativo
# plt.hist([s1, s2, s3], bins, label=['s1', 's2', 's3'])

plt.legend(loc = 'upper right')
plt.ylabel('Frequência')
plt.title('Comparação entre variáveis', loc = 'left')
