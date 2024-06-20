import os
from openpyxl import load_workbook
from fpdf import FPDF

def excel_to_pdf(input_excel, output_pdf):
    # Load the Excel workbook
    wb = load_workbook(filename=input_excel)

    # Initialize a PDF document
    pdf = FPDF()
    
    # Iterate through each sheet in the workbook
    for sheet in wb.sheetnames:
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Get the active worksheet
        ws = wb[sheet]
        
        # Extract data from the worksheet and add it to the PDF
        for row in ws.iter_rows(values_only=True):
            pdf.cell(200, 10, txt=" ".join(map(str,row)), ln=True)

    # Output the PDF to a file
    pdf.output(output_pdf)

if __name__ == "__main__":
    input_excel = "input_excel.xlsx"  # Replace with your input Excel file
    output_pdf = "output_pdf.pdf"     # Replace with desired output PDF file name
    
    excel_to_pdf(input_excel, output_pdf)
