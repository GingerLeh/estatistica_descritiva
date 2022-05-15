import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

#Geração dos dados
s1 = pd.Series([7, 7, 6, 2,	5, 4, 3, 7,	3, 1, 2, 4, 8, 6, 3, 7, 9, 6, 1, 3]) #gera uma série de dados
pd.DataFrame.head(s1)

s2 = pd.Series([3, 3, 5, 12, 3, 4, 10, 5, 4, 4, 3, 4, 8, 4, 5, 5, 6, 6, 4, 7])
pd.DataFrame.head(s2)

s3 = pd.Series([7, 7, 7, 8, 8, 7, 7, 7, 4, 8, 7, 8, 8, 9, 8, 8, 7, 9, 8, 8])
pd.DataFrame.head(s3)

##################################

#MODA 

moda1, count1 = stats.mode(s1) #mostra com o moda1 a moda e com o count a frequencia
# Converte o objeto para np.float64, que antes era uma array
moda1 = np.float64(moda1[0]) 
print(moda1)

# Código alternativo
# s1.mode()

moda2, count2 = stats.mode(s2)
# Converte o objeto para np.float64
moda2 = np.float64(moda2[0])
print(moda2)

moda3, count3 = stats.mode(s3)
# Converte o objeto para np.float64
moda3 = np.float64(moda3[0])
print(moda3)

#MEDIANA

# A mediana já é retornada como np.float64
mediana1 = np.median(s1)
print(mediana1)

# Código alternativo
# s2.median()
# A mediana já é retornada como np.float64
mediana2 = np.median(s2)
print(mediana2)


# A mediana já é retornada como np.float64
mediana3 = np.median(s3)
print(mediana3)


#MEDIA
media1 = np.mean(s1)
# Converte o objeto para np.float64
media1 = np.float64(media1)
print(media1)

# Código alternativo
# s1.mean(axis = 0)

media2 = np.mean(s2)
# Converte o objeto para np.float64
media2 = np.float64(media2)
print(media2)

# Código alternativo
# s2.mean(axis = 0)

media3 = np.mean(s3)
# Converte o objeto para np.float64
media3 = np.float64(media3)
print(media3)

# Código alternativo
# s3.mean(axis = 0)

#VIZUALIZAÇÃO 
xCoords = pd.Series([moda1, mediana1, media1], ['moda', 'mediana', 'media'])
print(xCoords.index)



#GRÁFICO ÚNICO
# Cria uma imagem vazia
fig = plt.figure()

# Plota o histograma
h = plt.hist(s1, bins = 5)

# Coloca título nos eixos
plt.title("Distribuição da variável S1", loc = 'left')

# Coloca nome nos eixos
plt.xlabel('s1')
plt.ylabel('Frequência')

# Define a cor das linhas
colors = ['r', 'k', 'y']

# Plota linhas verticais
for xc,xn,c in zip(xCoords, xCoords.index, colors):
    plt.axvline(x = xc, label = xn, c = c)
    
plt.legend()

#MULTIPLOS GRÁFICOS

# Cria a figura e os subplots
fig = plt.figure()
plt.subplots_adjust(hspace = 0.3, wspace = 0.4)
fig.suptitle('Comparação de distribuições, modas, médias e medianas', x=0.1, y=.95, horizontalalignment = 'left', verticalalignment = 'top')
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

# Cria os gráficos de histograma e acerta os nomes dos eixos
ax1.hist(s1, bins = 5)
ax1.set_xlabel('s1')
ax1.set_ylabel('Frequência')

ax2.hist(s2, bins = 5)
ax2.set_xlabel('s2')
ax2.set_ylabel('Frequência')

ax3.hist(s3, bins = 5)
ax3.set_xlabel('s3')
ax3.set_ylabel('Frequência')

# Cria as séries com as coordenadas das linhas verticais

xCoords1 = pd.Series([moda1, mediana1, media1], ['moda', 'mediana', 'media'])
xCoords2 = pd.Series([moda2, mediana2, media2], ['moda', 'mediana', 'media'])
xCoords3 = pd.Series([moda3, mediana3, media3], ['moda', 'mediana', 'media'])

# Plota as linhas

for xc,xn,c in zip(xCoords1, xCoords1.index, colors):
    ax1.axvline(x = xc, label = xn, c = c)
    
for xc,xn,c in zip(xCoords2, xCoords2.index, colors):
    ax2.axvline(x = xc, label = xn, c = c)
    
for xc,xn,c in zip(xCoords3, xCoords3.index, colors):
    ax3.axvline(x = xc, label = xn, c = c)
