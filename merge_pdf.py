import os
from PyPDF2 import PdfMerger

# Set the directory path where your PDF files are located
pdf_directory = "./individual_pdf"

# Get a list of all PDF files in the directory
pdf_files = [file for file in os.listdir(pdf_directory) if file.endswith('.pdf')]

# Sort the PDF files to merge them in a specific order if needed
pdf_files.sort()
print(pdf_files)
# Create a PdfMerger object
pdf_merger = PdfMerger()

# Loop through the PDF files and add them to the merger
for pdf_file in pdf_files:
    pdf_merger.append(os.path.join(pdf_directory, pdf_file))

# Specify the output file name and merge the PDFs
output_pdf = "merged.pdf"
pdf_merger.write(output_pdf)
pdf_merger.close()

print("PDF files merged successfully!")
