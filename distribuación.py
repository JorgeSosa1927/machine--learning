import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')
fig = plt.figure(figsize = (5,5))
w_0 = 1  ##Cintura del Haz
lam = 1  ##Longitud de onda
z = .2   ##Relacion del ancho del haz y la cintura
z_0 = (((2 * np.pi) / lam) * w_0 ** 2) / 4
w_z = w_0 * (1 + (z / z_0) ** 2)
def l(X,Y):
    return ((w_0/w_z)**2)*(((np.sqrt(2)*(X**2+Y**2))/w_z)**2)*np.exp((-2*(X**2+Y**2))/w_z**2) ##Funcion de Intensidad
def main():
    ax = plt.axes(projection='3d')
    x = np.linspace(-5, 5, 500)
    y = np.linspace(-5, 5, 500)
    X, Y = np.meshgrid(x, y)
    print(X)
    surf = ax.plot_surface(X, Y, l(X,Y), cmap = plt.cm.cividis)
    # Set axes label
    ax.set_zlim(-1, 1)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_xlabel('$x$', labelpad=20)
    ax.set_ylabel('$y$', labelpad=20)
    ax.set_zlabel('$z$', labelpad=20)
    ax.set_title('$Perfil-HLG$')
    fig.colorbar(surf, shrink=0.5, aspect=8)
    plt.show()
main()