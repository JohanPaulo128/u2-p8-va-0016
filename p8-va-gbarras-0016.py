import numpy as np
import matplotlib.pyplot as plt

diasX = ["Lun","Mar","Mie","Jue","Vie"]
califa_va_Y = [5,6,3,8,10]
plt.bar(diasX,califa_va_Y)
plt.title("Califas en VA de Johan Paulo Aros NC 0016")
plt.xlabel("Dias de la semana")
plt.ylabel("Calificaciones en VA")
plt.grid()
plt.show()