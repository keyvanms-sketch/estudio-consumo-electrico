import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import binom, norm

# 1. Crear el conjunto de datos

consumos = [
    30, 29, 31, 28, 32, 30, 27, 33, 29, 31,
    26, 34, 30, 28, 32, 29, 31, 30, 27, 33,
    30, 29, 31, 28, 32, 30, 30, 30, 30, 30
]

dias = list(range(1, 31))

datos = pd.DataFrame({
    "Dia": dias,
    "Consumo_kWh": consumos
})

print("DATOS DEL CONSUMO")
print(datos)

# 2. Guardar los datos en un CSV

datos.to_csv("consumo_30_dias.csv", index=False)

# 3. Calcular medidas estadísticas

media = datos["Consumo_kWh"].mean()
mediana = datos["Consumo_kWh"].median()
moda = datos["Consumo_kWh"].mode()[0]
desviacion = datos["Consumo_kWh"].std()
varianza = datos["Consumo_kWh"].var()
minimo = datos["Consumo_kWh"].min()
maximo = datos["Consumo_kWh"].max()
rango = maximo - minimo
q1 = datos["Consumo_kWh"].quantile(0.25)
q3 = datos["Consumo_kWh"].quantile(0.75)
ric = q3 - q1

print("\nRESULTADOS ESTADISTICOS")
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Desviacion estandar:", desviacion)
print("Varianza:", varianza)
print("Minimo:", minimo)
print("Maximo:", maximo)
print("Rango:", rango)
print("Primer cuartil:", q1)
print("Tercer cuartil:", q3)
print("Rango intercuartilico:", ric)

# 4. Distribucion normal

probabilidad_normal = norm.sf(
    33,
    loc=media,
    scale=desviacion
)

print("\nDISTRIBUCION NORMAL")
print("Probabilidad de superar 33 kWh:",
      probabilidad_normal)

# 5. Distribucion binomial

probabilidad_binomial = binom.sf(
    1,
    30,
    0.05
)

print("\nDISTRIBUCION BINOMIAL")
print("Probabilidad de dos o mas dias elevados:",
      probabilidad_binomial)

# 6. Contraste de hipotesis

resultado_t = stats.ttest_1samp(
    consumos,
    popmean=29,
    alternative="greater"
)

print("\nCONTRASTE DE HIPOTESIS")
print("Estadistico t:", resultado_t.statistic)
print("Valor p:", resultado_t.pvalue)

# 7. Grafica de lineas

plt.figure()
plt.plot(dias, consumos, marker="o")
plt.axhline(media, linestyle="--",
            label="Media")
plt.xlabel("Dia")
plt.ylabel("Consumo (kWh)")
plt.title("Consumo electrico diario")
plt.legend()
plt.grid()
plt.savefig("consumo_diario.png")
plt.show()

# 8. Histograma

plt.figure()
plt.hist(consumos, bins=np.arange(25.5, 35.5, 1),
         edgecolor="black")
plt.xlabel("Consumo (kWh)")
plt.ylabel("Frecuencia")
plt.title("Distribucion del consumo electrico")
plt.savefig("histograma.png")
plt.show()

# 9. Diagrama de caja

plt.figure()
plt.boxplot(consumos)
plt.ylabel("Consumo (kWh)")
plt.title("Diagrama de caja del consumo")
plt.savefig("diagrama_caja.png")
plt.show()

# 10. Grafico circular

niveles = [
    sum(26 <= x <= 28 for x in consumos),
    sum(29 <= x <= 31 for x in consumos),
    sum(32 <= x <= 34 for x in consumos)
]

nombres = ["Consumo bajo",
           "Consumo normal",
           "Consumo alto"]

plt.figure()
plt.pie(niveles, labels=nombres, autopct="%1.1f%%")
plt.title("Niveles de consumo")
plt.savefig("niveles_consumo.png")
plt.show()
