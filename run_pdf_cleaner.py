
print("Starting...")

if __name__ == '__main__':
    import argparse
    import pdf_edit
    
    parser = argparse.ArgumentParser(
        description="Clean PDF files downloaded from Studocu"
        )
    parser.add_argument(
        "folder", help="Path to the folder contains the PDFs"
        )

    args = parser.parse_args()
    pdf_edit.remove_first_page(args.folder)