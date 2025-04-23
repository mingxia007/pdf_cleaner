import os
from pypdf import PdfReader as pr, PdfWriter as pw
"""The files downloaded from Studocu always contain a page from the website 
that is irrelevant to the content. The filenames are also always mixed up. 
I wrote this script to solve the problem."""

def remove_first_page(source_dir):
    """
    Removes the first page of all PDF files in the directory, renames the 
    edited files to a numbered series, and stores them in a new directory.
    """
    # Create a new directory with the same name plus '_edited'
    # The new directory is in the same parent directory as the old one
    folder_name = os.path.basename(source_dir)
    parent_dir = os.path.dirname(source_dir)
    target_dir = os.path.join(parent_dir, f'{folder_name}_edited')
    os.makedirs(target_dir, exist_ok=True)

    for id, filename in enumerate(os.listdir(source_dir)):
        input_pdf_path = os.path.join(source_dir, filename)
        output_pdf_path = os.path.join(target_dir,f"{id}.pdf" )

        #Skip non-PDF files
        if not filename.lower().endswith('.pdf'):
            print(f"Skipping non-PDF file: {filename}")
            if filename =='.DS_Store':
                os.remove(input_pdf_path)
            continue

        with open(input_pdf_path, 'rb') as input_file:
            reader = pr(input_file) 
            writer = pw()

            #Add all pages except the first to the new file
            for i in range(1, len(reader.pages)):
                writer.add_page(reader.pages[i])
            with open(output_pdf_path, 'wb') as output_file:
                writer.write(output_file) 

        #Delete the old file
        os.remove(input_pdf_path)

    #Delete the old diretory when possible
    try:
        os.rmdir(source_dir)
    except OSError:
        print(f"Could not remove{source_dir}. It may not be empty.")
        
    print("Done! All Pdfs are converted successfully!")