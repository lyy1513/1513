import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False 
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.title('离散单位脉冲序列')
plt.xlabel("横坐标")
plt.ylabel("纵坐标")
def dwxl(t):
    r=np.where(t==0.0,1.0,0.0)
    return r
n=np.arange(-4,8)
plt.ylim(0,2)
plt.stem(n,dwxl(n))
plt.grid()
plt.show()