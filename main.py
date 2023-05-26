import re
import csv
import PyPDF2


def store_text_as_csv(text, output_file):
    lines = text.split('\n')

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for line in lines:
            writer.writerow([line])


pdf_path = 'C:/Users/Jan/Documents/Projekte/SchulenNRW/sozialindexstufen_der_einzelschulen.pdf'

# Open the PDF file
with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Extract text from each page
    all_text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        all_text += page.extract_text()

    # Store the text in a CSV file
    output_file = 'C:/Users/Jan/Documents/Projekte/SchulenNRW/CSV/GesamtePDF.csv'
    store_text_as_csv(all_text, output_file)
    print(f"Text has been stored in '{output_file}' as a CSV.")
