import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2docx import Converter
import os
import threading

def convert_pdf_to_docx(pdf_paths):
    try:
        for pdf_path in pdf_paths:
            # Validate PDF path
            if not os.path.exists(pdf_path):
                messagebox.showerror("Error", f"El archivo '{pdf_path}' no fue encontrado.")
                continue

            # Determine output DOCX file name
            pdf_name = os.path.basename(pdf_path)
            doc_name = os.path.splitext(pdf_name)[0] + ".docx"

            # Convert PDF to DOCX
            cv = Converter(pdf_path)
            output_path = os.path.join(os.path.dirname(pdf_path), doc_name)
            cv.convert(output_path, start=0, end=None)
            cv.close()

            # Mostrar mensaje de éxito en la consola (opcional)
            print(f"¡Documento DOCX creado satisfactoriamente como '{doc_name}'!")

        # Mostrar mensaje de éxito al finalizar todas las conversiones
        messagebox.showinfo("Éxito", "¡Todos los documentos PDF han sido convertidos a DOCX!")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error durante la conversión: {str(e)}")

def browse_pdf():
    # Función para seleccionar archivos PDF
    pdf_paths = filedialog.askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")])
    if pdf_paths:
        for pdf_path in pdf_paths:
            listbox_pdf_paths.insert(tk.END, pdf_path)

def convert():
    # Función para iniciar la conversión en un hilo separado
    pdf_paths = listbox_pdf_paths.get(0, tk.END)
    if pdf_paths:
        # Deshabilitar botones mientras se realiza la conversión
        button_browse.config(state=tk.DISABLED)
        button_convert.config(state=tk.DISABLED)

        # Iniciar la conversión en un hilo separado
        conversion_thread = threading.Thread(target=convert_pdf_to_docx, args=(pdf_paths,))
        conversion_thread.start()

        # Habilitar botones después de iniciar la conversión
        root.after(100, check_conversion_thread)

def check_conversion_thread():
    # Verificar si el hilo de conversión todavía está activo
    if threading.active_count() > 1:
        # Si el hilo aún está activo, revisar de nuevo después de 100 ms
        root.after(100, check_conversion_thread)
    else:
        # Si el hilo ha terminado, habilitar los botones nuevamente
        button_browse.config(state=tk.NORMAL)
        button_convert.config(state=tk.NORMAL)

# Crear la ventana principal
root = tk.Tk()
root.title("Convertir PDFs a DOCX")

# Crear y posicionar elementos en la ventana
label_pdf = tk.Label(root, text="Archivos PDF a convertir:")
label_pdf.grid(row=0, column=0, padx=10, pady=10)

listbox_pdf_paths = tk.Listbox(root, width=70, height=10, selectmode=tk.MULTIPLE)
listbox_pdf_paths.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

button_browse = tk.Button(root, text="Seleccionar PDFs", command=browse_pdf)
button_browse.grid(row=0, column=2, padx=10, pady=10)

button_convert = tk.Button(root, text="Convertir", command=convert)
button_convert.grid(row=1, column=2, padx=10, pady=10)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
