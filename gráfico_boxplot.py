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

#GRÁFICO ÚNICO
fig = plt.figure()
plt.boxplot(s2, showmeans = True) #para mostrar a média com o triângulo verde
plt.ylabel('Valores')

# Remove o valor do eixo x
plt.xticks([1], [''])

# Remove o tick do eixo x
plt.tick_params(axis = "x", which = "both", bottom = False, top = False)

plt.title('Gráfico Box-Plot da Variável s2', loc = 'left')


#GRÁFICO MÚLTIPLAS VARIÁVEIS EM UM GRÁFICO
fig = plt.figure()
plt.boxplot([s1, s2, s3], showmeans = True)
plt.xticks([1, 2, 3], ['s1', 's2', 's3'])
plt.ylabel('Valores')
plt.title('Gráfico Box-plot', loc = 'left')