import streamlit as st

def procesar_temperaturas(archivo_entrada):
    max_temperatura = None
    min_temperatura = None
    max_dia = None
    min_dia = None

    
    for linea in archivo_entrada:
        dia, temperatura = linea.strip().split(", ")
        temperatura = float(temperatura)

        
        if max_temperatura is None or temperatura > max_temperatura:
            max_temperatura = temperatura
            max_dia = dia

        
        if min_temperatura is None or temperatura < min_temperatura:
            min_temperatura = temperatura
            min_dia = dia

    return max_dia, max_temperatura, min_dia, min_temperatura

def main():
    st.title("Procesador de Temperaturas")

    
    uploaded_file = st.file_uploader("Cargar archivo de registro de temperaturas", type=["txt"])

    if uploaded_file is not None:
        
        file_contents = uploaded_file.getvalue().decode("utf-8").splitlines()

        max_dia, max_temperatura, min_dia, min_temperatura = procesar_temperaturas(file_contents)

        
        st.write(f"Día de temperatura máxima: {max_dia}, {max_temperatura}")
        st.write(f"Día de temperatura mínima: {min_dia}, {min_temperatura}")

if __name__ == "__main__":
    main()
