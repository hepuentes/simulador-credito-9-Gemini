import streamlit as st
import pandas as pd

# Datos de las líneas de crédito (ajusta según tus necesidades)
LINEAS_DE_CREDITO = {
    "LoansiFlex": {
        # ... tus datos
    },
    "Microflex": {
        # ... tus datos
    }
}

def calcular_cuota(monto, tasa_mensual, plazo):
    """Calcula la cuota mensual de un préstamo.

    Args:
        monto (float): Monto del préstamo.
        tasa_mensual (float): Tasa de interés mensual en formato decimal.
        plazo (int): Número de cuotas.

    Returns:
        float: Cuota mensual.
    """

    cuota = (monto * tasa_mensual) / (1 - (1 + tasa_mensual) ** -plazo)
    return cuota

def crear_tabla_amortizacion(monto, tasa_mensual, plazo, cuota):
    """Crea una tabla de amortización.

    Args:
        monto (float): Monto del préstamo.
        tasa_mensual (float): Tasa de interés mensual en formato decimal.
        plazo (int): Número de cuotas.
        cuota (float): Cuota mensual.

    Returns:
        pd.DataFrame: Tabla de amortización.
    """

    saldo = monto
    interes_total = 0
    capital_total = 0
    data = {'Cuota': [], 'Interés': [], 'Capital': [], 'Saldo': []}
    for i in range(1, plazo + 1):
        interes = saldo * tasa_mensual
        capital = cuota - interes
        saldo -= capital
        interes_total += interes
        capital_total += capital
        data['Cuota'].append(cuota)
        data['Interés'].append(interes)
        data['Capital'].append(capital)
        data['Saldo'].append(saldo)
    return pd.DataFrame(data)

# Función principal de la aplicación
def main():
    # Título de la aplicación
    st.title("Simulador de Crédito")

    # Selección de la línea de crédito
    tipo_credito = st.selectbox("Selecciona la Línea de Crédito", options=LINEAS_DE_CREDITO.keys())
    detalles = LINEAS_DE_CREDITO[tipo_credito]

    # ... resto de tu código (entrada de datos, cálculos, etc.)

    # Botón de simulación
    if st.button("Simular"):
        # ... tus cálculos

        # Crear la tabla de amortización
        tabla_amortizacion = crear_tabla_amortizacion(monto, detalles["tasa_mensual"] / 100, plazo, cuota)
        st.dataframe(tabla_amortizacion)

        # ... otros elementos visuales

if __name__ == "__main__":
    main()
