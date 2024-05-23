import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Configurar la sesión
if 'data' not in st.session_state:
    st.session_state['data'] = []

# Función para añadir datos al historial
def add_to_history(category, subcategories, amounts):
    entry = {
        'date': datetime.now(),
        'category': category,
        'subcategories': subcategories,
        'amounts': amounts
    }
    st.session_state['data'].append(entry)

# Título del proyecto
st.title('Planificador de Presupuesto')

# Opciones de categorías
categories = ['Presupuesto Personal', 'Presupuesto Familiar', 'Presupuesto para Eventos', 'Presupuesto Empresarial', 'Presupuesto de Viaje', 'Otro']

# Selección de categoría principal
category = st.selectbox('Selecciona una categoría de presupuesto', categories)

if category == 'Otro':
    category = st.text_input('Ingresa el nombre de la categoría de presupuesto')

# Categorías de gastos predeterminadas
default_subcategories = ['Vivienda', 'Alimentos', 'Transporte', 'Entretenimiento', 'Otros']

# Selección de subcategorías
st.header('Categorías de Gastos')
subcategories = st.multiselect('Selecciona las categorías de gastos', default_subcategories)

if 'Otros' in subcategories:
    other_subcategory = st.text_input('Ingresa el nombre de la nueva categoría de gastos')
    if other_subcategory:
        subcategories.append(other_subcategory)
    subcategories.remove('Otros')

# Entrada de datos de gastos
st.header('Ingreso de Datos')
amounts = {}
for subcategory in subcategories:
    amounts[subcategory] = st.number_input(f'Gastos en {subcategory}', min_value=0.0, step=0.01)

# Botón para agregar al historial
if st.button('Agregar al Historial'):
    add_to_history(category, subcategories, amounts)
    st.success('Datos agregados al historial')

# Visualización de datos
st.header('Visualización de Datos')
total_expenses = sum(amounts.values())
st.write(f'**Total de Gastos:** ${total_expenses:.2f}')

# Gráfico de distribución de gastos
expenses_df = pd.DataFrame(list(amounts.items()), columns=['Categoría', 'Monto'])
st.bar_chart(expenses_df.set_index('Categoría'))

# Historial
st.header('Historial')
timeframes = {
    'Último día': datetime.now() - timedelta(days=1),
    'Últimos 3 días': datetime.now() - timedelta(days=3),
    'Última semana': datetime.now() - timedelta(weeks=1),
    'Último mes': datetime.now() - timedelta(days=30),
    'Últimos 3 meses': datetime.now() - timedelta(days=90),
    'Últimos 6 meses': datetime.now() - timedelta(days=180),
    'Último año': datetime.now() - timedelta(days=365)
}

# Selección de periodo de historial
timeframe = st.selectbox('Selecciona el periodo del historial', list(timeframes.keys()))

# Filtrar y mostrar historial
start_date = timeframes[timeframe]
filtered_data = [entry for entry in st.session_state['data'] if entry['date'] >= start_date]

if filtered_data:
    for entry in filtered_data:
        st.write(f"**Fecha:** {entry['date'].strftime('%Y-%m-%d %H:%M:%S')}")
        st.write(f"**Categoría de Presupuesto:** {entry['category']}")
        st.write(f"**Gastos:**")
        for subcategory, amount in entry['amounts'].items():
            st.write(f"- {subcategory}: ${amount:.2f}")
else:
    st.write('No hay datos en el historial para el periodo seleccionado.')
