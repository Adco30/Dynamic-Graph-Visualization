import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

root = tk.Tk()

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111, projection='3d')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

a, b, c = 1, 1, 1
elev, azim = 0, 0 

def generate_curve(a, b, c, t):
    x = a * np.sin(t)
    y = b * np.cos(t) + c * np.sin(t)**2
    z = c * np.sin(t)**2
    return x, y, z

def plot_view():
    global elev, azim
    t = np.linspace(0, 2*np.pi, 100)
    x, y, z = generate_curve(a, b, c, t)

    x_grid = np.linspace(min(x), max(x), 100)
    y_grid = np.linspace(min(y), max(y), 100)
    x_mesh, y_mesh = np.meshgrid(x_grid, y_grid)

    z_values = np.zeros((100, 100))
    for i in range(100):
        for j in range(100):
            t = np.arctan2(y_mesh[i, j], x_mesh[i, j])
            z_values[i, j] = generate_curve(a, b, c, t)[2]

    ax.clear()
    ax.view_init(elev=elev, azim=azim) 
    ax.plot_surface(x_mesh, y_mesh, z_values, cmap='coolwarm')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    fig.canvas.draw()
    canvas.draw_idle()

def on_scroll(event):
    global elev, azim
    elev -= event.step * 5
    azim += event.step * 5
    plot_view()

canvas.mpl_connect('scroll_event', on_scroll)

plot_view()
tk.mainloop()