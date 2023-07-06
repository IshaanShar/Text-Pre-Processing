import PyPDF2

def extract_text_from_pdf(file_path): 
    text = ""
    
    # Open the PDF file in binary mode
    with open(file_path, "rb") as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Iterate over each page in the PDF
        for page_number in range(len(pdf_reader.pages)):
            # Extract the text from the current page
            page = pdf_reader.pages[page_number]
            page_text = page.extract_text()
            
            # Append the extracted text to the result
            text += page_text
    
    return text

def save_text_to_file(text, output_file_path):
    with open(output_file_path, "w") as file:
        file.write(text)

# Example usage
pdf_file_path = "/path/inputfile"
output_file_path = "/path/outputfile"

extracted_text = extract_text_from_pdf(pdf_file_path)
save_text_to_file(extracted_text, output_file_path)
