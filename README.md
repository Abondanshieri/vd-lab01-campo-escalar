# Laboratorio 01 · Visualización de campo escalar

De un número por punto a mapas de colores e isolíneas

**Visualización de Datos** · Escuela Profesional de Ingeniería de Sistemas · Universidad Nacional del Altiplano – Puno
Estudiante: Franco Abondanshieri Arela Mamani · 25 de noviembre de 2026

Se visualizó una temperatura simulada sobre una grilla de 25 × 25 puntos mediante un mapa de calor, isolíneas y una comparación de paletas (`viridis` y `plasma`). Tres retos exploraron la resolución de la grilla, la saturación de la escala de color y la información de las isolíneas.

## Estructura

| Ruta | Contenido |
|---|---|
| `notebooks/LAB_01_Arela_Mamani_Franco.ipynb` | Cuaderno ejecutado: bloques guiados, retos, respuestas y conclusiones |
| `src/LAB_01_Arela_Mamani_Franco.py` | El mismo código en texto plano |
| `anexos/figuras/` | 6 figuras PNG extraídas del cuaderno |
| `anexos/salidas/` | Salidas de consola de cada bloque |
| `informe/` | Informe del laboratorio en `.docx` y `.pdf` |

## Cómo reproducirlo

```bash
pip install numpy matplotlib jupyter
jupyter notebook notebooks/LAB_01_Arela_Mamani_Franco.ipynb
```

También puede abrirse en Google Colab (*Archivo → Abrir cuaderno → GitHub*) y ejecutarse bloque por bloque con `Shift + Enter`.
Los datos son sintéticos: se generan en el propio código, por lo que no hay archivos de datos externos.
