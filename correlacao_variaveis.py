import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


#CARREGANDO DADOS

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
## Nome das colunas foi adquirido do arquivo aut-mp.names
## https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.names
names = ['mpg', 'cyl', 'disp', 'hp', 'weight', 'acc', 'year', 'origin', 'name']
df = pd.read_table(url, header = None, delim_whitespace = True, names = names)
pd.DataFrame.head(df)

#ESTATISTICAS DESCRITIVAS
desc = df.describe()
print(desc)

#Seleção das variáveis numéricas
num = df.select_dtypes(include = 'number')
pd.DataFrame.head(num)

# Cria a figura e os subplots
fig = plt.figure()
plt.subplots_adjust(hspace = 0.3, wspace = 0.4)
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# Cria os gráficos de histograma e acerta os nomes dos eixos
ax1.hist(num['year'], bins = 5)
ax2.hist(num['origin'], bins = 5)

#Remover colunas 'year' e 'origin'
numClean = num.drop(['year', 'origin'], axis = 1) #axis = 1 é para dropar as colunas
numClean.head() #numClean passou a ser o dataset agora

#CORRELAÇÃO ENTRE DUAS VARIÁVEIS

plt.close('all')
ig = plt.figure()
plt.scatter(numClean['weight'], numClean['disp'])
plt.xlabel('Weight [lbs]')
plt.ylabel('Displacement [m]')
np.corrcoef(numClean['weight'], numClean['disp'])
np.corrcoef(numClean['weight'], numClean['disp'])[0,1]

#CORRELAÇÃO ENTRE VÁRIAS VARIÁVEIS
sns.pairplot(numClean)
corrMatPd = numClean.corr() #mostra de forma numérica as correlações (pandas)
print(corrMatPd)