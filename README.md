# PDF Cleaner

#### PDF Cleaner CLI is a simple Python script that removes the first page from all PDF files in a folder and renames the cleaned PDFs to a numbered sequence.

## Features
- Remove the first page of each PDF in the selected folder.
- Rename the cleaned PDFs in a numbered sequence (e.g., 0.pdf, 1.pdf, etc.).


Simple command-line tool.

## Requirements
- Python 3.x
- pypdf library (for PDF processing)

## Installation
-  Clone this repository (or download the project files).
`git clone <repository_url>`
-  Install the required Python library:
`pip install pypdf`

## How to Use
- Open the terminal and navigate to the folder containing the run_pdf_cleaner.py script.
- Run the script with the path to the folder containing the PDFs:
- python3 run_pdf_cleaner.py '/path/to/your/folder'

 #### Example:

`python3 run_pdf_cleaner.py '/Users/you/Documents/studocu_pdfs'`

## Troubleshooting

- No PDFs found? Make sure the folder contains valid PDF files.
- Permission issues? Ensure you have permission to read and write in the folder.