### PDF TOOLKIT

This Python script provides a comprehensive set of utilities for working with PDF files, including converting PDFs to images, extracting text via OCR, and converting image files back to PDFs. It also organizes the output into structured folders, making it easy to manage and access the results.

#### Features:
- **Convert PDFs to Images:** Converts each page of a PDF to a high-quality PNG image.
- **Extract Text from PDFs:** Utilizes Optical Character Recognition (OCR) to extract text from image-based PDFs.
- **Convert Images to PDFs:** Converts individual image files or a folder of images into a single PDF, sorted by image names in ascending order.
- **Organized Output:** Saves all outputs (PDFs, images, and text files) in a structured folder setup, located in the same directory as the script.

#### Folder Structure:
- **output/**
  - **pdfs/**: Contains the generated PDF files.
  - **texts/**: Contains the extracted text files.
  - **images/**: Contains the converted images.

#### Requirements:
- Python 3.x
- [pytesseract](https://github.com/madmaze/pytesseract) (for OCR)
- [pdf2image](https://github.com/Belval/pdf2image)
- [Pillow](https://python-pillow.org/)

#### Installation:
1. Install the required libraries:
   ```bash
   pip install pytesseract pdf2image pillow
   ```

2. Download and install Tesseract OCR (for text extraction). Refer to the [installation guide](https://github.com/tesseract-ocr/tesseract).

#### Usage:
1. Place your PDF files in a folder and run the script.
2. The script will generate output in the same directory under an `output` folder, containing subfolders for `pdfs`, `texts`, and `images`.
