"""Laboratorio 01 · Visualización de campo escalar — código plano (exportado del cuaderno).
Ejecutar bloque por bloque: cada bloque reutiliza las variables de los anteriores."""

# ===== Entorno =====
import sys, platform
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 110          # nitidez de las figuras exportadas
print("Python    :", platform.python_version())
print("NumPy     :", np.__version__)
print("Matplotlib:", matplotlib.__version__)
plt.show = lambda *a, **k: None  # ejecución sin ventanas


# ===== Bloque 1. Preparar el entorno y crear una grilla =====
import numpy as np                 # Permite calcular con arreglos y matrices
import matplotlib.pyplot as plt    # Permite generar gráficos

# Generamos 25 posiciones horizontales y 25 verticales
x = np.linspace(-5, 5, 25)       # Valores desde -5 hasta 5
y = np.linspace(-5, 5, 25)       # Valores desde -5 hasta 5

# Combinamos cada valor de X con cada valor de Y
X, Y = np.meshgrid(x, y)

print("Forma de X:", X.shape)
print("Total de posiciones:", X.size)
print("Posición del centro:", X[12, 12], Y[12, 12])


# ===== Bloque 2. Asignar una temperatura a cada punto =====
# Un valor de temperatura para cada posición
T = 20 + 12 * np.exp(-(X**2 + Y**2) / 8)

print("Forma del campo escalar:", T.shape)
print("Temperatura en el centro:", round(T[12, 12], 2), "°C")
print("Temperatura mínima:", round(T.min(), 2), "°C")
print("Temperatura máxima:", round(T.max(), 2), "°C")

# Visualizamos los números de una pequeña zona
print("Temperaturas de la zona central:")
print(np.round(T[11:14, 11:14], 1))


# ===== Bloque 3. Convertir los números en un mapa de colores =====
plt.figure(figsize=(7, 5))
mapa = plt.imshow(T, origin="lower", extent=[-5, 5, -5, 5],
                  cmap="viridis", vmin=20, vmax=32)
plt.colorbar(mapa, label="Temperatura (°C)")
plt.title("Campo escalar: temperatura simulada")
plt.xlabel("Posición X")
plt.ylabel("Posición Y")
plt.show()


# ===== Bloque 4. Dibujar isolíneas =====
plt.figure(figsize=(7, 5))
lineas = plt.contour(X, Y, T, levels=[22, 24, 26, 28, 30],
                     colors="navy")
plt.clabel(lineas, inline=True, fontsize=9, fmt="%.0f °C")
plt.title("Isolíneas: puntos de igual temperatura")
plt.xlabel("Posición X")
plt.ylabel("Posición Y")
plt.axis("equal")
plt.show()


# ===== Bloque 5. Comparar dos mapas de colores =====
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
for ax, paleta in zip(axes, ["viridis", "plasma"]):
    imagen = ax.imshow(T, origin="lower", extent=[-5, 5, -5, 5],
                       cmap=paleta, vmin=20, vmax=32)
    ax.set_title("Paleta: " + paleta)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    fig.colorbar(imagen, ax=ax, label="°C")
plt.tight_layout()
plt.show()


# ===== Reto 1. Grilla de 25 a 50 puntos =====
# Nueva grilla de 50 x 50 (2 500 posiciones) con la misma fórmula
x50 = np.linspace(-5, 5, 50)
y50 = np.linspace(-5, 5, 50)
X50, Y50 = np.meshgrid(x50, y50)
T50 = 20 + 12 * np.exp(-(X50**2 + Y50**2) / 8)

c = T50.shape[0] // 2          # índice "central" sin escribir un 12 a mano
print("Forma:", T50.shape, "| posiciones:", T50.size)
print("Punto central T[c, c] ->", round(T50[c, c], 3), "°C en (",
      round(X50[c, c], 3), ",", round(Y50[c, c], 3), ")")
print("Máximo real de la grilla:", round(T50.max(), 3), "°C")
print("Paso entre puntos -> 25:", round(10/24, 3), " | 50:", round(10/49, 3))

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
for ax, campo, titulo in zip(axes, [T, T50], ["Grilla 25 x 25", "Grilla 50 x 50"]):
    im = ax.imshow(campo, origin="lower", extent=[-5, 5, -5, 5],
                   cmap="viridis", vmin=20, vmax=32, interpolation="nearest")
    ax.set_title(titulo)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    fig.colorbar(im, ax=ax, label="°C")
plt.tight_layout()
plt.show()


# ===== Reto 2. Cambiar el 12 por 18 en la fórmula =====
# Mismo campo, pero con amplitud 18 en lugar de 12
T18 = 20 + 18 * np.exp(-(X**2 + Y**2) / 8)

print("Centro:", round(T18[12, 12], 2), "°C | máximo:", round(T18.max(), 2),
      "°C | mínimo:", round(T18.min(), 2), "°C")
saturadas = int((T18 > 32).sum())
print("Celdas por encima de 32 °C (fuera de la escala original):", saturadas, "de", T18.size)

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
for ax, vmax, titulo in zip(axes, [32, 38],
                            ["Escala original (vmax = 32)", "Escala ajustada (vmax = 38)"]):
    im = ax.imshow(T18, origin="lower", extent=[-5, 5, -5, 5],
                   cmap="viridis", vmin=20, vmax=vmax)
    ax.set_title(titulo)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    fig.colorbar(im, ax=ax, label="°C")
plt.tight_layout()
plt.show()


# ===== Reto 3. Seis isolíneas en lugar de cinco =====
niveles6 = [22, 24, 26, 28, 30, 31]          # se añadió el nivel de 31 °C
radios = np.sqrt(8 * np.log(12 / (np.array(niveles6) - 20)))   # radio de cada círculo (despejado de la fórmula)

for nivel, radio in zip(niveles6, radios):
    print(f"{nivel} °C -> radio {radio:.2f}")
print("Variación de temperatura por unidad de distancia entre isolíneas consecutivas:")
for (n1, r1), (n2, r2) in zip(zip(niveles6, radios), zip(niveles6[1:], radios[1:])):
    print(f"  {n1} -> {n2} °C: {(n2 - n1) / (r1 - r2):.2f} °C/unidad")

fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
for ax, niveles, titulo in zip(axes, [[22, 24, 26, 28, 30], niveles6], ["5 isolíneas", "6 isolíneas"]):
    lineas = ax.contour(X, Y, T, levels=niveles, colors="navy")
    ax.clabel(lineas, inline=True, fontsize=8, fmt="%.0f °C")
    ax.set_title(titulo)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_aspect("equal")
plt.tight_layout()
plt.show()
