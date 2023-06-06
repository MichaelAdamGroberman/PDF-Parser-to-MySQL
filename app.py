import PyPDF2
import pandas as pd
import mysql.connector

# Connect to MySQL
cnx = mysql.connector.connect(
    host = 'your_host', 
    user = 'your_username',
    password = 'your_password',
    database = 'your_database'
)
cursor = cnx.cursor()

# Define a function to parse the PDF
def parse_pdf(file):
    pdf_file = open(file, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    text = ""
    for i in range(read_pdf.getNumPages()):
        page = read_pdf.getPage(i)
        text += page.extractText()
    return text

# Use the function to parse the PDF
pdf_text = parse_pdf('path_to_your_pdf')

# You might need to process the extracted text to better fit your database schema
# For simplicity, let's imagine you just want to save the whole text into one column

# Prepare the INSERT statement
insert_stmt = "INSERT INTO your_table (column_name) VALUES (%s)"

# Execute the statement
cursor.execute(insert_stmt, (pdf_text,))

# Make sure data is committed to the database
cnx.commit()

# Close connections
cursor.close()
cnx.close()
