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


##QUANTIS
s175 = np.quantile(s1,0.75)
s275 = np.quantile(s2,0.75)
s375 = np.quantile(s3,0.75)