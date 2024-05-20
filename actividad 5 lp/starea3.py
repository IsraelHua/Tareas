import streamlit as st

def convertir_a_soles(precio_dolares):
    # Tasa de conversión de dólares a soles
    tasa_conversion = 3.85

    # Convertir precio de dólares a soles
    precio_soles = precio_dolares * tasa_conversion

    return precio_soles

def main():
    st.title("Conversor de precios de dólares a soles")

    
    uploaded_file = st.file_uploader("Cargar archivo de precios en dólares", type=["txt"])

    if uploaded_file is not None:
        
        file_contents = uploaded_file.getvalue().decode("utf-8").splitlines()

        
        output_prices = []

       
        for line in file_contents:
            # Dividir la línea en producto y precio en dólares
            producto, precio_dolares = line.strip().split(", ")
            precio_dolares = float(precio_dolares)

           
            precio_soles = convertir_a_soles(precio_dolares)

            
            output_prices.append(f"{producto}, {precio_soles:.2f}")

        
        st.header("Precios convertidos a soles:")
        for price in output_prices:
            st.write(price)

        
        output_text = "\n".join(output_prices)
        st.download_button(
            label="Descargar precios en soles",
            data=output_text,
            file_name="precios_soles.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()

