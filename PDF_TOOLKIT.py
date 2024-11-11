import os
from pdf2image import convert_from_path
import pytesseract
from PIL import Image

# Set the path to the Tesseract executable (if not set in PATH)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'  # Update this path if needed

def convert_pdf_to_images(pdf_path, output_images_folder):
    """
    Convert a PDF to a series of images, one for each page.
    """
    if not os.path.exists(output_images_folder):
        os.makedirs(output_images_folder)
    
    try:
        # Convert PDF to images
        images = convert_from_path(pdf_path, dpi=300)  # Adjust DPI for quality
        
        for i, page in enumerate(images):
            image_path = os.path.join(output_images_folder, f"page_{i + 1}.png")
            page.save(image_path, "PNG")
            print(f"Saved: {image_path}")
    except Exception as e:
        print(f"Error converting PDF to images: {e}")


def convert_pdf_to_text(pdf_path, output_texts_folder):
    """
    Convert a PDF file to a text file using OCR for image-based PDFs.
    """
    try:
        # Convert PDF to images (one per page)
        images = convert_from_path(pdf_path)

        # Extract text from each image using OCR
        text = ""
        for img in images:
            text += pytesseract.image_to_string(img)
        
        # Define output txt file path
        base_name = os.path.basename(pdf_path).replace('.pdf', '.txt')
        txt_path = os.path.join(output_texts_folder, base_name)
        
        # Write text to a .txt file
        with open(txt_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(text)
        print(f"Saved text for '{pdf_path}' to '{txt_path}'")
    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")


def process_pdfs_in_folder(folder_path, output_folder, operation):
    """
    Scan the folder for PDF files and perform either image conversion or text extraction.
    """
    os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist

    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith('.pdf'):
            pdf_path = os.path.join(folder_path, file_name)
            
            if operation == "images":
                convert_pdf_to_images(pdf_path, output_folder)
            elif operation == "text":
                convert_pdf_to_text(pdf_path, output_folder)
            else:
                print("Invalid operation. Choose 'images' or 'text'.")


def convert_images_to_pdf(images_folder, output_pdf_path):
    """
    Convert a folder of images into a single PDF, sorted by image names in ascending order.
    """
    try:
        # Get a sorted list of images by filename
        image_files = sorted([f for f in os.listdir(images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

        # Load the images and convert to a PDF
        images = [Image.open(os.path.join(images_folder, image_file)) for image_file in image_files]
        
        # Convert images to a single PDF
        images[0].save(output_pdf_path, save_all=True, append_images=images[1:], resolution=100.0, quality=95)
        print(f"Images converted to PDF: {output_pdf_path}")
    except Exception as e:
        print(f"Error converting images to PDF: {e}")


def main():
    """
    Main function to choose the operation and folder paths.
    """
    # User inputs for folder and operation
    folder_path = input("Enter the folder path containing PDFs: ").strip()
    operation = input("Enter operation ('images' for converting PDFs to images, 'text' for extracting text, 'pdf' for converting images to a PDF): ").strip().lower()

    # Determine the output folder based on the operation
    output_folder = os.path.join(os.path.dirname(folder_path), "output")
    os.makedirs(output_folder, exist_ok=True)  # Create the main output folder
    
    # Define specific subfolders within the output folder
    if operation == "images":
        output_images_folder = os.path.join(output_folder, "images")
        process_pdfs_in_folder(folder_path, output_images_folder, operation)
    elif operation == "text":
        output_texts_folder = os.path.join(output_folder, "texts")
        process_pdfs_in_folder(folder_path, output_texts_folder, operation)
    elif operation == "pdf":
        output_images_folder = os.path.join(output_folder, "images")
        image_folder_path = input("Enter the folder path containing images for PDF conversion: ").strip()
        output_pdf_path = os.path.join(output_folder, "pdfs", "output.pdf")
        convert_images_to_pdf(image_folder_path, output_pdf_path)
    else:
        print("Invalid operation selected. Exiting.")
        return


if __name__ == "__main__":
    main()
