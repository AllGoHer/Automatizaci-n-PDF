import streamlit as st
from fpdf import FPDF
from datetime import datetime
import base64

# Configuración de la página
st.set_page_config(page_title="Generador de Cuentos Mágicos", page_icon="📚", layout="wide")

# Título principal
st.title("📚 Generador de Cuentos Infantiles Mágicos")
st.markdown("---")

# Crear 3 columnas para los cuentos
col1, col2, col3 = st.columns(3)

# ============================================
# CUENTO 1: El Dragón de los Colores
# ============================================
with col1:
    st.subheader("🐉 El Dragón de los Colores")
    
    cuento1 = """
Érase una vez un dragón llamado Sparky que tenía un problema muy peculiar:
¡no podía echar fuego! En lugar de llamas, echaba colores.

Un día, el pueblo estaba triste porque la primavera tardaba en llegar.
Todo era gris y aburrido. Sparky, viendo la tristeza de todos,
tomó una gran bocanada de aire y... ¡PUF!

De su boca salió un arcoíris completo que pintó el cielo.
Rojo para las flores, azul para el río, amarillo para el sol,
y verde para los árboles. El pueblo entero sonrió.

Sparky descubrió que su magia no era para luchar,
sino para traer alegría y color al mundo.
Desde entonces, cada año pinta la primavera.
"""
    
    st.text_area("Cuento 1: El Dragón de los Colores", cuento1, height=250)
    
    if st.button("📥 Descargar Cuento 1", key="btn1"):
        # Crear PDF
        pdf = FPDF()
        pdf.add_page()
        
        # Encabezado
        pdf.set_font("Arial", 'B', 24)
        pdf.set_text_color(220, 50, 50)  # Rojo
        pdf.cell(0, 15, "El Dragón de los Colores", ln=True, align='C')
        
        # Imagen decorativa (usando caracteres)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, "🐉", ln=True, align='C')
        
        # Autor y fecha
        pdf.set_font("Arial", 'I', 12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 10, f"Por: Magia Infantil • {datetime.now().strftime('%d/%m/%Y')}", ln=True, align='C')
        
        # Línea separadora
        pdf.line(10, 45, 200, 45)
        
        # Contenido del cuento
        pdf.ln(15)
        pdf.set_font("Arial", size=14)
        pdf.set_text_color(0, 0, 0)  # Negro
        
        # Dividir el texto en líneas
        lineas = cuento1.split('\n')
        for linea in lineas:
            if linea.strip():  # Si no está vacía
                pdf.multi_cell(0, 8, linea)
                pdf.ln(2)
        
        # Pie de página
        pdf.set_y(-30)
        pdf.set_font("Arial", 'I', 10)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(0, 10, "Cuento generado con ❤️ para niños soñadores", align='C')
        
        # Guardar PDF
        pdf_file = "cuento1_dragon_colores.pdf"
        pdf.output(pdf_file)
        
        # Crear enlace de descarga
        with open(pdf_file, "rb") as f:
            pdf_bytes = f.read()
        
        b64 = base64.b64encode(pdf_bytes).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="{pdf_file}">¡Haz clic aquí si la descarga no inicia automáticamente!</a>'
        
        st.success("✅ PDF generado exitosamente!")
        st.markdown(href, unsafe_allow_html=True)
        st.balloons()

# ============================================
# CUENTO 2: La Luna que Quería Ser Sol
# ============================================
with col2:
    st.subheader("🌙 La Luna que Quería Ser Sol")
    
    cuento2 = """
Luna era una niña-luna brillante pero infeliz.
Todas las noches veía al Sol iluminar el día
y quería ser tan brillante como él.

Un día, decidió bajar a la Tierra para preguntar.
Preguntó a los búhos, a los grillos y a los niños dormidos:
"¿Cómo puedo ser como el Sol?"

Un sabio búho le respondó:
"Luna, tú tienes tu propia magia.
Miras por los sueños de los niños,
guías a los viajeros en la oscuridad,
y pintas de plata los paisajes nocturnos."

Esa noche, Luna miró su reflejo en el lago
y vio lo hermosa que era. Comprendió que
cada uno brilla a su manera y en su momento.
"""
    
    st.text_area("Cuento 2: La Luna que Quería Ser Sol", cuento2, height=250)
    
    if st.button("📥 Descargar Cuento 2", key="btn2"):
        pdf = FPDF()
        pdf.add_page()
        
        pdf.set_font("Arial", 'B', 24)
        pdf.set_text_color(50, 100, 200)  # Azul
        pdf.cell(0, 15, "La Luna que Quería Ser Sol", ln=True, align='C')
        
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, "🌙", ln=True, align='C')
        
        pdf.set_font("Arial", 'I', 12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 10, f"Por: Magia Infantil • {datetime.now().strftime('%d/%m/%Y')}", ln=True, align='C')
        
        pdf.line(10, 45, 200, 45)
        pdf.ln(15)
        
        pdf.set_font("Arial", size=14)
        pdf.set_text_color(0, 0, 0)
        
        lineas = cuento2.split('\n')
        for linea in lineas:
            if linea.strip():
                pdf.multi_cell(0, 8, linea)
                pdf.ln(2)
        
        # Agregar ilustración ASCII
        pdf.set_font("Courier", size=10)
        pdf.ln(5)
        pdf.cell(0, 5, "       ___", ln=True)
        pdf.cell(0, 5, "     /     \\", ln=True)
        pdf.cell(0, 5, "    /       \\", ln=True)
        pdf.cell(0, 5, "   /  luna   \\", ln=True)
        pdf.cell(0, 5, "   \\   🌙    /", ln=True)
        pdf.cell(0, 5, "    \\       /", ln=True)
        pdf.cell(0, 5, "     \\_____/", ln=True)
        
        pdf.set_y(-30)
        pdf.set_font("Arial", 'I', 10)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(0, 10, "Cuento para aprender a valorar nuestra propia luz", align='C')
        
        pdf_file = "cuento2_luna_sol.pdf"
        pdf.output(pdf_file)
        
        with open(pdf_file, "rb") as f:
            pdf_bytes = f.read()
        
        b64 = base64.b64encode(pdf_bytes).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="{pdf_file}">¡Haz clic aquí si la descarga no inicia automáticamente!</a>'
        
        st.success("✅ PDF generado exitosamente!")
        st.markdown(href, unsafe_allow_html=True)
        st.balloons()

# ============================================
# CUENTO 3: El Árbol de los Abrazos
# ============================================
with col3:
    st.subheader("🌳 El Árbol de los Abrazos")
    
    cuento3 = """
En el bosque Encantado había un árbol muy especial:
el Árbol de los Abrazos. Sus ramas eran suaves como algodón
y sus hojas susurraban canciones de cuna.

Cada vez que un animalito se sentía triste,
solo tenía que abrazar su tronco y automáticamente
se llenaba de calidez y alegría.

Un día llegó Pinito, un pino pequeño que se sentía
solo porque había perdido a su familia en una tormenta.

El Árbol de los Abrazos lo envolvió con sus ramas
y le dijo: "Aquí tienes una familia nueva:
los pájaros cantores, las ardillas traviesas
y yo, que seré tu abuelo árbol."

Pinito creció fuerte y feliz, aprendiendo que
la familia no siempre es la que naces, sino la que encuentras.
"""
    
    st.text_area("Cuento 3: El Árbol de los Abrazos", cuento3, height=250)
    
    if st.button("📥 Descargar Cuento 3", key="btn3"):
        pdf = FPDF()
        pdf.add_page()
        
        pdf.set_font("Arial", 'B', 24)
        pdf.set_text_color(50, 150, 50)  # Verde
        pdf.cell(0, 15, "El Árbol de los Abrazos", ln=True, align='C')
        
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, "🌳", ln=True, align='C')
        
        pdf.set_font("Arial", 'I', 12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 10, f"Por: Magia Infantil • {datetime.now().strftime('%d/%m/%Y')}", ln=True, align='C')
        
        pdf.line(10, 45, 200, 45)
        pdf.ln(15)
        
        pdf.set_font("Arial", size=14)
        pdf.set_text_color(0, 0, 0)
        
        lineas = cuento3.split('\n')
        for linea in lineas:
            if linea.strip():
                pdf.multi_cell(0, 8, linea)
                pdf.ln(2)
        
        # Agregar moraleja
        pdf.ln(10)
        pdf.set_font("Arial", 'B', 12)
        pdf.set_text_color(100, 50, 150)  # Púrpura
        pdf.cell(0, 10, "Moraleja:", ln=True)
        pdf.set_font("Arial", 'I', 12)
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 8, "El amor y la familia se encuentran en los lugares y corazones más inesperados.")
        
        pdf.set_y(-30)
        pdf.set_font("Arial", 'I', 10)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(0, 10, "Un cuento sobre amor, familia y aceptación", align='C')
        
        pdf_file = "cuento3_arbol_abrazos.pdf"
        pdf.output(pdf_file)
        
        with open(pdf_file, "rb") as f:
            pdf_bytes = f.read()
        
        b64 = base64.b64encode(pdf_bytes).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="{pdf_file}">¡Haz clic aquí si la descarga no inicia automáticamente!</a>'
        
        st.success("✅ PDF generado exitosamente!")
        st.markdown(href, unsafe_allow_html=True)
        st.balloons()

# ============================================
# SECCIÓN EXTRA: Descargar los 3 juntos
# ============================================
st.markdown("---")
st.subheader("🎁 Paquete Completo de Cuentos")

if st.button("📚 Descargar los 3 Cuentos Juntos", type="primary"):
    # Crear un PDF con los 3 cuentos
    pdf = FPDF()
    
    # Cuento 1
    pdf.add_page()
    pdf.set_font("Arial", 'B', 24)
    pdf.set_text_color(220, 50, 50)
    pdf.cell(0, 15, "Colección de Cuentos Mágicos", ln=True, align='C')
    
    pdf.set_font("Arial", 'B', 20)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)
    pdf.cell(0, 10, "1. El Dragón de los Colores", ln=True)
    
    pdf.set_font("Arial", size=12)
    lineas = cuento1.split('\n')
    for linea in lineas:
        if linea.strip():
            pdf.multi_cell(0, 6, linea)
    
    # Cuento 2
    pdf.add_page()
    pdf.set_font("Arial", 'B', 20)
    pdf.cell(0, 10, "2. La Luna que Quería Ser Sol", ln=True)
    
    pdf.set_font("Arial", size=12)
    lineas = cuento2.split('\n')
    for linea in lineas:
        if linea.strip():
            pdf.multi_cell(0, 6, linea)
    
    # Cuento 3
    pdf.add_page()
    pdf.set_font("Arial", 'B', 20)
    pdf.cell(0, 10, "3. El Árbol de los Abrazos", ln=True)
    
    pdf.set_font("Arial", size=12)
    lineas = cuento3.split('\n')
    for linea in lineas:
        if linea.strip():
            pdf.multi_cell(0, 6, linea)
    
    # Página final
    pdf.add_page()
    pdf.set_font("Arial", 'B', 18)
    pdf.cell(0, 20, "Fin de la Colección", ln=True, align='C')
    pdf.set_font("Arial", 'I', 14)
    pdf.multi_cell(0, 10, "\n\nQue estos cuentos traigan magia, enseñanzas y sueños coloridos a los pequeños lectores.")
    
    pdf_file = "coleccion_3_cuentos_magicos.pdf"
    pdf.output(pdf_file)
    
    with open(pdf_file, "rb") as f:
        pdf_bytes = f.read()
    
    b64 = base64.b64encode(pdf_bytes).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="{pdf_file}">📥 Haz clic para descargar los 3 cuentos en un solo PDF</a>'
    
    st.success("🎉 ¡Colección completa generada!")
    st.markdown(href, unsafe_allow_html=True)
    st.snow()

# ============================================
# INSTRUCCIONES
# ============================================
st.markdown("---")
with st.expander("📖 ¿Cómo usar esta aplicación?"):
    st.write("""
    ### Instrucciones simples:
    1. **Lee** los cuentos en cada columna
    2. **Haz clic** en el botón de descarga del cuento que quieras
    3. **Espera** a que se genere el PDF (verás globos de celebración 🎈)
    4. **Descarga** el archivo PDF
    5. **Imprime** o lee en tu dispositivo
    
    ### Características de los PDFs:
    - Título colorido
    - Fecha de creación automática
    - Formato profesional
    - Diseño amigable para niños
    - Se pueden imprimir fácilmente
    
    ### Requisitos:
    - Solo necesitas un navegador web
    - No requiere instalación adicional
    - Totalmente gratuito
    """)

st.caption("✨ Hecho con magia, código y mucho cariño para los niños del mundo ✨")