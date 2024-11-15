import streamlit as st
import pandas as pd

# ... (tu diccionario de líneas de crédito y otros datos)

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

# ... (resto del código)

# Botón de simulación estilizado
if st.button("Simular"):
    # ... (cálculos)

    # Crear una tabla de amortización
    tabla_amortizacion = crear_tabla_amortizacion(monto, detalles["tasa_mensual"] / 100, plazo, cuota)
    st.dataframe(tabla_amortizacion)

    # Crear un gráfico simple (ejemplo)
    fig = go.Figure(data=go.Scatter(x=list(range(1, plazo + 1)), y=tabla_amortizacion['Saldo']))
    fig.update_layout(title='Evolución del Saldo', xaxis_title='Cuota', yaxis_title='Saldo')
    st.plotly_chart(fig)