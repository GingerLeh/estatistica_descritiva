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

#AMPLITUDE
range1 = np.ptp(s1)
print(range1)
range2 = np.ptp(s2)
print(range2)
range3 = np.ptp(s3)
print(range3)

#VARINÂNCIA
# NumPy calcula por padrão variância populacional. Para amostra, ddof = 1
var1 = np.var(s1, ddof = 1)
# Converte para np.float64
var1 = np.float64(var1)
print(var1)

# Código alternativo
#s1.var(axis = 0)

var2 = np.var(s2, ddof = 1)
# Converte para np.float64
var2 = np.float64(var2)
print(var2)

var3 = np.var(s3, ddof = 1)
# Converte para np.float64
var3 = np.float64(var3)
print(var3)

#DESVIO PADRÃO
sd1 = np.std(s1, ddof = 1)
sd1 = np.float64(sd1)
print(sd1)

# Código alternatico
# s1.std()
sd2 = np.std(s2, ddof = 1)
sd2 = np.float64(sd2)
print(sd2)

sd3 = np.std(s3, ddof = 1)
sd3 = np.float64(sd3)
print(sd3)