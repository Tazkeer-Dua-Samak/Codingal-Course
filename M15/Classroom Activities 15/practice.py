import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-1, 1, 0.2) 
y = x*x*x 
plt.plot(x, y, 'g', linewidth=3, label='y=x^3')
plt.legend()
plt.show()