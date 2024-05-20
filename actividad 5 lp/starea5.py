import streamlit as st

def procesar_ventas(archivo_entrada):
    total_ventas = 0
    cantidad_ventas = 0
    max_venta = None
    min_venta = None
    max_dia = None
    min_dia = None

    # Leer las ventas del archivo
    for linea in archivo_entrada:
        dia, venta = linea.strip().split(", ")
        venta = int(venta)

        
        total_ventas += venta
        cantidad_ventas += 1

       
        if max_venta is None or venta > max_venta:
            max_venta = venta
            max_dia = dia

        
        if min_venta is None or venta < min_venta:
            min_venta = venta
            min_dia = dia

    
    promedio_ventas = total_ventas / cantidad_ventas

    return total_ventas, promedio_ventas, max_dia, max_venta, min_dia, min_venta

def main():
    st.title("Procesador de Ventas")

    
    uploaded_file = st.file_uploader("Cargar archivo de ventas diarias", type=["txt"])

    if uploaded_file is not None:
        
        file_contents = uploaded_file.getvalue().decode("utf-8").splitlines()

        total_ventas, promedio_ventas, max_dia, max_venta, min_dia, min_venta = procesar_ventas(file_contents)

        
        st.write(f"Venta total: {total_ventas}")
        st.write(f"Promedio de ventas: {promedio_ventas:.2f}")
        st.write(f"Día de mayor venta: {max_dia}, {max_venta}")
        st.write(f"Día de menor venta: {min_dia}, {min_venta}")

if __name__ == "__main__":
    main()
