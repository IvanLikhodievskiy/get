import numpy as np
import matplotlib.pyplot as plt

with open("settings.txt", "r") as settings:

    tmp = [float(i) for i in settings.read().split("\n")]

data_array = np.loadtxt("data.txt", dtype = float)
data_array *= tmp[1]

time = np.linspace(0.0, tmp[0] * (len(data_array) - 1) / 1000 , len(data_array))
charge = time[data_array.argmax()]
discharge = time[len(time) - 1] - charge

fig, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(time, data_array, color = "blue", marker = "o",
    linestyle = "solid", markersize = 6, markevery = 25, label = "U(t)")

plt.xlabel("t, s", fontsize = 14)
plt.xlim(0, time.max() + 0.5)

plt.ylabel("U, V", fontsize = 14)
plt.ylim(data_array.min(), data_array.max() + 0.1)

ax.grid(which = "major", color = "grey", linestyle = "solid")
ax.grid(which = "minor", color = "grey", linestyle = "dashed")

ax.minorticks_on()

plt.annotate(f"Charging time: {round(charge, 2)} s", (46, 2.25), fontsize = 12)
plt.annotate(f"Discharging time: {round(discharge, 2)} s", (46, 2), fontsize = 12)

ax.set_title("Graph U(t)")

plt.legend(loc = "best", fontsize = 14)

fig.savefig("graph.svg")
plt.show()