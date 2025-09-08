import matplotlib as mlt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

price = [10, 322, 665, 339, 725, 946, 238, 829]
year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007]
plt.plot(year, price)
# plt.show()
b = (np.random.random(8))*1000
plt.plot(year, b)
plt.title(" runs of players")
plt.xlabel("bhosdi valo ka year")
plt.ylabel('bhosdi valo ke runes')
plt.plot(year, price, color='blue')
plt.show()
# b1 = (np.random.random(16))*1000
# plt.plot(price1, b1)
# plt.show()
see = pd.read_csv(r'C:\Users\Employee Sample Data.csv', encoding='ISO-8859-1')
print(see)



