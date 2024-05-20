import streamlit as st

def procesar_horas_trabajo(archivo_entrada):
    horas_trabajo = {}

    
    for linea in archivo_entrada:
        empleado, horas = linea.strip().split(", ")
        horas = int(horas)

        
        if empleado in horas_trabajo:
            horas_trabajo[empleado] += horas
        else:
            horas_trabajo[empleado] = horas

    return horas_trabajo

def main():
    st.title("Procesador de Horas de Trabajo")

    
    uploaded_file = st.file_uploader("Cargar archivo de registro de horas de trabajo", type=["txt"])

    if uploaded_file is not None:
        
        file_contents = uploaded_file.getvalue().decode("utf-8").splitlines()

        horas_trabajo = procesar_horas_trabajo(file_contents)

        
        st.header("Horas totales trabajadas por empleado:")
        for empleado, horas_totales in horas_trabajo.items():
            st.write(f"{empleado}, Horas Totales: {horas_totales}")

if __name__ == "__main__":
    main()
