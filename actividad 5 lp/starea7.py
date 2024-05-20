import streamlit as st

def contar_errores(archivo_entrada):
    conteo_errores = {}

    
    for linea in archivo_entrada:
        error = linea.strip()
        if error in conteo_errores:
            conteo_errores[error] += 1
        else:
            conteo_errores[error] = 1

    return conteo_errores

def main():
    st.title("Contador de Errores en Archivo de Log")

    
    uploaded_file = st.file_uploader("Cargar archivo de log", type=["txt"])

    if uploaded_file is not None:
        
        file_contents = uploaded_file.getvalue().decode("utf-8").splitlines()

        conteo_errores = contar_errores(file_contents)

        
        st.header("Resumen de errores:")
        for error, cantidad in conteo_errores.items():
            st.write(f"{error}: {cantidad}")

if __name__ == "__main__":
    main()
