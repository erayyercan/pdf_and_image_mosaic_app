# Mosaic Project

## Overview
The **Mozaic Project** is a Python-based application that applies a mosaic effect to detected faces in image or PDF files. It uses OpenCV for face detection and PyMuPDF for handling PDF files, making it versatile for processing various file formats. The processed images can be saved with user-defined file names.

---

## Features
- **Face Detection:** Detects faces in images and applies a mosaic effect.
- **PDF Support:** Extracts images from PDF files and processes each page.
- **User-Friendly Interface:** Uses `Tkinter` for file selection and saving.
- **Image Resizing:** Resizes processed images to a standard size (600x800 pixels).

---

## Requirements
Ensure you have the following libraries installed:

- Python 3.6+
- OpenCV
- NumPy
- PyMuPDF
- Tkinter (default in Python installations)

To install the required libraries, run:
```bash
pip install opencv-python numpy pymupdf
```
---

## How It Works

### 1. File Selection

The user selects a file using a file dialog. Supported formats:

- Image files: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.gif`

- PDF files: `.pdf`

### 2. Processing

 #### PDF FILES:

- Pages are converted to images using PyMuPDF.

- Face detection and mosaic are applied to each page.

- Processed pages are displayed and can be saved as separate image files.

 #### IMAGE FILES:

- The selected image is processed with face detection and mosaic.

- The processed image is displayed and can be saved.

### 3. Face Detection

- Uses OpenCV's `haarcascade_frontalface_default.xml` for detecting faces. Detected faces are replaced with a mosaic effect using resizing techniques.

---

## How to Run

1- Save the script as `mozaic.py.`

2- Run the script:
```bash
python mozaic.py
```
3- Select a file from the file dialog.

4- Process the file and save the results.

---

## File Structure

- `mozaic.py`: Main script.

---

## Code Details

### Key Functions

1- `get_file_path()`: Opens a file dialog to select a file.

2- `apply_mosaic(image, rect, size)`: Applies a mosaic effect to a given region.

3- `process_pdf(pdf_path)`: Extracts and processes images from a PDF file.

4- `process_image(image)`: Detects faces and applies a mosaic effect to an image.

5- `mozaic()`: Main function that integrates file selection, processing, and saving.

---

## Example Usage

### Processing a PDF File

  1- Select a PDF file.

  2- View processed pages one by one.

  3- Save each page as an image file.

### Processing an Image File

  1- Select an image file.

  2- View the processed image.

  3- Save the result with a custom file name.

---

## Notes

- Ensure the `haarcascade_frontalface_default.xml` file is available in your OpenCV installation directory.

- File selection and saving dialogs depend on the Tkinter library.

---

## License

This project is open-source and available under the [MIT License](https://opensource.org/license/mit).

---

## Contact

For any questions or feedback, feel free to contact the project author.
