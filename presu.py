import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title='Aplicación de Presupuestos', layout='centered')

# Título 
st.title('Controla tus Finanzas')

# Simulación de conexión de cuentas
st.sidebar.header('Conectar Cuentas Financieras')
tarjeta_credito = st.sidebar.text_input('Tarjeta de Crédito', 'Ingrese su numero de targeta de credito')
prestamos = st.sidebar.text_input('ingrese su codigo de seguridad (CVV)', 'Ingrese su codigo de seguridad')

# Presupuestación
st.header('Presupuestación')

# Tipo de presupuesto
tipo_presupuesto = st.selectbox('Seleccione el tipo de presupuesto', ['Semanal', 'Mensual'])

categories = ['Alimentos', 'Transporte', 'Entretenimiento', 'Salud', 'Educación', 'Otros']
presupuesto = {}

# Ingresar los valores de presupuesto
for category in categories:
    presupuesto[category] = st.text_input(f'Presupuesto para {category} ({tipo_presupuesto.lower()})', value="", key=category)

# Convertir los valores de presupuesto a numéricos
for category in categories:
    try:
        presupuesto[category] = float(presupuesto[category])
    except ValueError:
        presupuesto[category] = 0.0

# Inicializar el estado de sesión para las transacciones si no existe
if 'transacciones' not in st.session_state:
    st.session_state.transacciones = pd.DataFrame(columns=['Fecha', 'Categoría', 'Monto', 'Tipo'])

# Seguimiento de Gastos e Ingresos
st.header('Seguimiento de Gastos e Ingresos')

def agregar_transaccion():
    with st.form(key='Agregar Transacción'):
        fecha = st.date_input('Fecha', datetime.date.today())
        categoria = st.selectbox('Categoría', categories)
        monto = st.text_input('Monto', value="", key='Monto')
        tipo = st.selectbox('Tipo', ['Gasto', 'Ingreso'])
        submit = st.form_submit_button('Agregar')

        if submit:
            if monto:
                monto = float(monto)
                nueva_transaccion = pd.DataFrame({
                    'Fecha': [fecha],
                    'Categoría': [categoria],
                    'Monto': [monto],
                    'Tipo': [tipo]
                })
                st.session_state.transacciones = pd.concat([st.session_state.transacciones, nueva_transaccion], ignore_index=True)
            else:
                st.warning('Por favor, ingrese el monto.')

agregar_transaccion()

# Mostrar transacciones
if not st.session_state.transacciones.empty:
    st.subheader('Transacciones')
    st.dataframe(st.session_state.transacciones)

# Alertas y Recordatorios
st.header('Alertas y Recordatorios')
recordatorios = st.text_area('Añadir recordatorios', 'Pago de alquiler, Pagar tarjeta de crédito')

# Informes Financieros
st.header('Informes Financieros')
if st.button('Generar Informe'):
    st.subheader('Historial de Gastos e Ingresos')
    st.dataframe(st.session_state.transacciones)

    # Filtrar las transacciones según el tipo de presupuesto
    hoy = datetime.date.today()
    if tipo_presupuesto == 'Semanal':
        inicio_periodo = hoy - datetime.timedelta(days=hoy.weekday())
    elif tipo_presupuesto == 'Mensual':
        inicio_periodo = hoy.replace(day=1)

    transacciones_periodo = st.session_state.transacciones[st.session_state.transacciones['Fecha'] >= pd.Timestamp(inicio_periodo)]
    
    # Calcular totales de gastos e ingresos por categoría
    resumen_periodo = transacciones_periodo.groupby(['Categoría', 'Tipo'])['Monto'].sum().unstack(fill_value=0)
    resumen_periodo['Total Gastos'] = resumen_periodo.get('Gasto', 0)
    resumen_periodo['Total Ingresos'] = resumen_periodo.get('Ingreso', 0)

    # Comparar con el presupuesto
    comparacion_presupuesto = {}
    for category in categories:
        gastos = resumen_periodo.at[category, 'Total Gastos'] if category in resumen_periodo.index else 0
        ingresos = resumen_periodo.at[category, 'Total Ingresos'] if category in resumen_periodo.index else 0
        balance = ingresos - gastos
        diferencia = presupuesto[category] - gastos
        comparacion_presupuesto[category] = {
            'Presupuesto': presupuesto[category],
            'Gastos': gastos,
            'Ingresos': ingresos,
            'Balance': balance,
            'Diferencia con Presupuesto': diferencia
        }

    comparacion_presupuesto_df = pd.DataFrame(comparacion_presupuesto).transpose()
    st.subheader(f'Comparación con Presupuesto {tipo_presupuesto.lower()}')
    st.dataframe(comparacion_presupuesto_df)
    
    # Evaluar si estamos dentro del presupuesto o en números rojos
    en_numeros_rojos = comparacion_presupuesto_df[comparacion_presupuesto_df['Diferencia con Presupuesto'] < 0]
    if not en_numeros_rojos.empty:
        st.warning('Estás en números rojos nos vamos a la ruina:')
        st.dataframe(en_numeros_rojos)
    else:
        st.success('Ta piola.')

# Mostrar información de cuentas conectadas en un lugar poco visible
st.write("")
st.write("")
st.subheader('Información de Cuentas Conectadas')
if tarjeta_credito:
    st.write(f"Tarjeta de Crédito: {tarjeta_credito}")
if prestamos:
    st.write(f"Préstamos: {Cvv}")
