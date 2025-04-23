import os

from pypdf import PdfReader as pr, PdfWriter as pw
"""The files downloaded from studocu always contain a page from the website 
that is irrelevant to the content.The names are also always mixed up. I wrote 
this script to solve the problem."""

def remove_first_page(source_dir):
    """Remove the first page of all pdf files in the directory and rename them 
    to a numbered series. 
    """
    id = 0
    folder_name = os.path.basename(source_dir)
    parent_dir = os.path.dirname(source_dir)
    target_dir = os.path.join(parent_dir, f'{folder_name}_edit')
    os.makedirs(target_dir, exist_ok=True)

    for filename in os.listdir(source_dir):

        input_pdf_path = os.path.join(source_dir, filename)
        output_pdf_path = os.path.join(target_dir,f"{id}.pdf" )

        if not filename.lower().endswith('.pdf'):
            print(f"Skipping non-PDF file: {filename}")
            if filename =='.DS_Store':
                os.remove(input_pdf_path)
            continue

        with open(input_pdf_path, 'rb') as input_file:
            #with neednt to open and close file
            reader = pr(input_file) #Object
            writer = pw()#Object

            #add all of pages except the first
            for i in range(1, len(reader.pages)):
                writer.add_page(reader.pages[i])
            #name the new file    
            with open(output_pdf_path, 'wb') as output_file:
                writer.write(output_file) 

        os.remove(input_pdf_path)
        id += 1

    try:
        os.rmdir(source_dir)
    except OSError:
        print(f"Could not remove{source_dir}. It may not be empty.")
        
    print("Done! All of the pdfs are converted sucessfully!")


remove_first_page('/Users/m.lin/Desktop/cost_accounting/example')