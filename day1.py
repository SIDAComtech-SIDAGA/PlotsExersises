from matplotlib import pyplot as plt
import numpy as np
import random

x = np.random.randint(1,25,2)
print(x)


y = [15,13,2,3,5,6,1,1]


plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y)
plt.xticks(range(25,50))
plt.yticks(range(min(y),max(y)+1))

plt.show()