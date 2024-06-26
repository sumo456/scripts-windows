# Scripts de Manipulación de PDF y Conversión a DOCX

Este repositorio contiene dos scripts en Python que permiten realizar operaciones específicas con archivos PDF utilizando la biblioteca `PyPDF2` y convertir PDFs a documentos DOCX utilizando `pdf2docx`. A continuación se detalla cómo utilizarlos y cómo asegurarse de tener las dependencias necesarias instaladas.

## Instalación de Dependencias

Antes de ejecutar los scripts, asegúrate de tener instalado Python en tu sistema. Además, necesitarás instalar `pip`, el gestor de paquetes de Python.

Para instalar las bibliotecas requeridas, ejecuta el siguiente comando en tu terminal o símbolo del sistema:

pip install -r requirements.txt



Este comando instalará automáticamente las siguientes dependencias:

- `PyPDF2`: Utilizada para manipular archivos PDF en el primer script.
- `tkinter`: Biblioteca estándar de Python para crear interfaces gráficas.
- `pdf2docx`: Utilizada para convertir archivos PDF a DOCX en el segundo script.

Si no tienes `pip` instalado, asegúrate de instalarlo primero. Puedes encontrar instrucciones detalladas para la instalación de `pip` en [este enlace](https://pip.pypa.io/en/stable/installation/).

## Uso de los Scripts

### Script 1: PDF Unificación

Este script permite agregar varios archivos PDF y fusionarlos en uno solo.

Para ejecutar el script, sigue estos pasos:

1. Abre una terminal o símbolo del sistema.
2. Navega al directorio donde se encuentra el script `PDFUnificacion.py`.
3. Asegúrate de haber instalado las dependencias con el comando `pip install -r requirements.txt`.
4. Ejecuta el script con el siguiente comando:

python PDFUnificacion.py


5. Sigue las instrucciones en la ventana de la interfaz gráfica para agregar archivos PDF y fusionarlos.

### Script 2: PDF to DOCX Converter

Este script convierte archivos PDF seleccionados a documentos DOCX.

Para ejecutar el script, sigue estos pasos:

1. Abre una terminal o símbolo del sistema.
2. Navega al directorio donde se encuentra el script `PDFtoWORD.py`.
3. Asegúrate de haber instalado las dependencias con el comando `pip install -r requirements.txt`.
4. Ejecuta el script con el siguiente comando:

python PDFtoWORD.py




5. Sigue las instrucciones en la ventana de la interfaz gráfica para seleccionar los archivos PDF y convertirlos a DOCX.
