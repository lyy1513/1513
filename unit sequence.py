import numpy as np
import matplotlib.pyplot as plt
def dwxl(t):
    r=np.where(t==0.0,1.0,0.0)
    return r
n=np.arange(-4,8)
plt.ylim(0,2)
plt.stem(n,dwxl(n))
plt.show()