print("\n📊 REPORTE DE VENTAS")
print("----------------------")
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("ventas.csv")

# Crear columna de ingresos
df["ingreso"] = df["cantidad"] * df["precio"]

# Ingreso total
ingreso_total = df["ingreso"].sum()
print("💰 Ingreso total:", ingreso_total)

# Producto más vendido
producto_top = df.groupby("producto")["cantidad"].sum().idxmax()
print("🏆 Producto más vendido:", producto_top)

# Ventas por producto
ventas_producto = df.groupby("producto")["ingreso"].sum()
ventas_producto.to_csv("reporte.csv")
print("📁 Reporte exportado como reporte.csv")

# Gráfica
ventas_producto.plot(kind="bar", title="Ingresos por producto")
plt.xlabel("Producto")
plt.ylabel("Ingresos")
plt.show()
