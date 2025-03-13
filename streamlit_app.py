# prompt: Crea un código streamlit

import streamlit as st

st.title("Calculadora de Precios")

# Precio por centímetro cuadrado
precio_por_cm2 = 240 / (58 * 100)

st.header("Área Fija (10x10 cm)")
area_fija = 10 * 10
precio_area_fija = precio_por_cm2 * area_fija
st.write(f"El precio de un área de 10x10 cm es: {precio_area_fija:.2f} pesos")


st.header("Área Personalizada")
ancho = st.number_input("Introduce el ancho del área en cm:", min_value=0.0, value=1.0)
largo = st.number_input("Introduce el largo del área en cm:", min_value=0.0, value=1.0)
area_nueva = ancho * largo
precio_nuevo = precio_por_cm2 * area_nueva
st.write(f"El precio de un área de {ancho}x{largo} cm es: {precio_nuevo:.2f} pesos")


st.header("Costo de Planchas")
precio_plancha = 10
costo_total_planchas = 0
num_planchas = st.number_input("Número de planchas aplicadas:", min_value=0, value=0, step=1)
costo_total_planchas = num_planchas * precio_plancha
st.write(f"El costo total de las planchas es: {costo_total_planchas} pesos")


st.header("Venta de Camisetas")
camisetas = {
    "Chica": 80,
    "Mediana": 50,
    "Grande": 60,
    "Extra Grande": 65
}

st.write("Opciones de camisetas:")
for talla, precio in camisetas.items():
  st.write(f"- Talla: {talla}, Precio: ${precio}")

tallas_seleccionadas = st.multiselect("Selecciona las tallas de camisetas:", list(camisetas.keys()))

costo_total_camisetas = 0
for talla in tallas_seleccionadas:
    costo_total_camisetas += camisetas[talla]

st.write(f"\nCosto total de las camisetas seleccionadas: ${costo_total_camisetas}")

st.header("Costo Total")
costo_total_general = precio_nuevo + costo_total_planchas + costo_total_camisetas
st.write(f"El costo total de la orden es: ${costo_total_general}")
