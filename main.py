import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from math import comb

# --- функция для подсчёта числа областей ---
def regions(n, d):
    """Вычисляет число областей R(n,d) = sum_{k=0}^{d} C(n,k)"""
    return sum(comb(n, k) for k in range(d + 1))

# --- запрос параметров у пользователя ---
d = int(input("Введите размерность пространства (1, 2 или 3): "))
n = int(input("Введите количество гиперплоскостей: "))

# --- 1D случай ---
if d == 1:
    points = sorted(np.random.uniform(-5, 5, n))
    plt.figure(figsize=(8, 2))
    plt.hlines(1, -6, 6, colors='gray', linestyles='dashed')
    plt.plot(points, [1]*n, 'ro', markersize=6)
    plt.title(f"Разбиение прямой {n} точками", fontsize=13, pad=10)
    plt.xlim(-6, 6)
    plt.yticks([])
    plt.text(0, 0.7, f"Количество областей: R({n},1) = {regions(n,1)}",
             fontsize=12, ha='center', color='blue')
    plt.show()

# --- 2D случай ---
elif d == 2:
    lines = []
    for i in range(n):
        a, b, c = np.random.uniform(-2, 2, 3)
        lines.append((a, b, c))

    x = np.linspace(-5, 5, 400)
    plt.figure(figsize=(7, 7))
    for (a, b, c) in lines:
        if abs(b) < 1e-3:
            x0 = -c / a
            plt.axvline(x0, color='black', lw=1)
        else:
            y = (-a * x - c) / b
            plt.plot(x, y, lw=1, color='black')

    plt.title(f"Разбиение плоскости {n} прямыми", fontsize=13, pad=10)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.grid(True)
    plt.text(0, -5.5, f"Количество областей: R({n},2) = {regions(n,2)}",
             fontsize=12, ha='center', color='blue')
    plt.show()

# --- 3D случай ---
elif d == 3:
    np.random.seed(42)
    planes = []
    for i in range(n):
        a, b, c = np.random.uniform(-2, 2, 3)
        if abs(c) < 0.3:
            c += np.sign(c) * 0.5 if c != 0 else 0.5
        d_ = np.random.uniform(-3, 3)
        planes.append((a, b, c, d_))

    x = np.linspace(-5, 5, 60)
    y = np.linspace(-5, 5, 60)
    X, Y = np.meshgrid(x, y)

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    colors = [cm.viridis(i / n) for i in range(n)]

    for i, (a, b, c, d_) in enumerate(planes):
        Z = (-a * X - b * Y - d_) / c
        ax.plot_surface(X, Y, Z, alpha=0.5, facecolor=colors[i],
                        rstride=1, cstride=1, edgecolor='none')

    ax.set_title(f"Разбиение пространства {n} плоскостями", fontsize=14, pad=20)
    ax.set_xlabel('X', labelpad=10)
    ax.set_ylabel('Y', labelpad=10)
    ax.set_zlabel('Z', labelpad=10)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-5, 5)
    ax.view_init(elev=25, azim=35)

    # добавляем подпись под графиком
    fig.text(0.5, 0.05, f"Количество областей: R({n},3) = {regions(n,3)}",
             ha='center', fontsize=12, color='blue')

    plt.tight_layout()
    plt.show()

else:
    print("Ошибка: размерность должна быть 1, 2 или 3.")
