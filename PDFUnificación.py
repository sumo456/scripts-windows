import PyPDF2
import tkinter as tk
from tkinter import filedialog, messagebox

class PDFMergeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merge Tool")

        self.input_files = []

        # Frame principal
        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.pack(padx=10, pady=10)

        # Etiqueta de bienvenida
        self.label = tk.Label(self.main_frame, text="Welcome to the PDF Merge Tool", font=("Helvetica", 14))
        self.label.pack(pady=10)

        # Botones para agregar y fusionar PDFs
        self.add_button = tk.Button(self.main_frame, text="Add PDFs", command=self.add_pdfs, font=("Helvetica", 12))
        self.add_button.pack(pady=10)

        self.merge_button = tk.Button(self.main_frame, text="Merge PDFs", command=self.merge_pdfs, font=("Helvetica", 12))
        self.merge_button.pack(pady=10)

    def add_pdfs(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
        if files:
            self.input_files.extend(files)
            messagebox.showinfo("Files Added", f"{len(files)} PDF(s) added.")

    def merge_pdfs(self):
        if not self.input_files:
            messagebox.showwarning("No Files Selected", "Please add PDF files to merge.")
            return

        output_filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_filename:
            pdf_merger = PyPDF2.PdfMerger()
            for file in self.input_files:
                try:
                    with open(file, 'rb') as pdf_file:
                        pdf_merger.append(pdf_file)
                except FileNotFoundError:
                    print(f"Warning: File '{file}' not found. Skipping...")
                    messagebox.showwarning("File Not Found", f"Warning: File '{file}' not found. Skipping...")

            with open(output_filename, 'wb') as output_file:
                pdf_merger.write(output_file)

            print(f"PDFs merged successfully! Output file: {output_filename}")
            messagebox.showinfo("Success", f"PDFs merged successfully! Output file: {output_filename}")

            # Limpiar lista de archivos seleccionados después de la fusión
            self.input_files = []

def main():
    root = tk.Tk()
    app = PDFMergeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()