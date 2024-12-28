import fitz  # PyMuPDF
import cv2
import numpy as np
from tkinter import Tk, filedialog
import os

# select file from user

def get_file_path():
    Tk().withdraw()  # hide Tkinter window
    file_path = filedialog.askopenfilename(title="Bir Dosya Seçin", 
                                           filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff;*.gif"), 
                                                     ("PDF files", "*.pdf")])
    return file_path

# apply mosaic function

def apply_mosaic(image, rect, size=15):
    (x, y, w, h) = rect
    face = image[y:y+h, x:x+w]
    face = cv2.resize(face, (size, size), interpolation=cv2.INTER_LINEAR)
    face = cv2.resize(face, (w, h), interpolation=cv2.INTER_NEAREST)
    image[y:y+h, x:x+w] = face
    return image

# pdf2image

def process_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    images = []
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()  # Convert page to pixmap (image)
        
        # Convert to NumPy array format (with correct color channel dimensions)
        
        img = np.frombuffer(pix.samples, dtype=np.uint8)  # bytes'ı numpy array'e dönüştür
        if pix.n == 4:  # if RGBA format
            img = img.reshape(pix.height, pix.width, 4)  # 4 channel (RGBA)
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)  # convert to BGR for OpenCv
        elif pix.n == 3:  # if RGB format
            img = img.reshape(pix.height, pix.width, 3)  # 3 channel (RGB)
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  
        images.append(img)
    return images

# face detection and mosaic

def process_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        image = apply_mosaic(image, (x, y, w, h))
    
    # resize the image
    
    target_width = 600
    target_height = 800
    image = cv2.resize(image, (target_width, target_height), interpolation=cv2.INTER_AREA)
    
    return image

# main process

def mozaic():
    file_path = get_file_path()
    if not file_path:
        print("Dosya Seçilmedi.")
        return
    
    # process PDF file
    
    if file_path.lower().endswith(".pdf"):
        images = process_pdf(file_path)
        for i, image in enumerate(images):
            print(f"Sayfa {i + 1} İşleniyor...")
            processed_image = process_image(image)  
            cv2.imshow(f"Sayfa {i + 1}", processed_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # create a different file name for each page
            
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", 
                                                     filetypes=[("Image files", "*.jpg *.jpeg *.png")],
                                                     initialfile=f"Sayfa_{i + 1}.jpg")
            if save_path:
                cv2.imwrite(save_path, processed_image)
                print(f"Sayfa {i + 1} Kaydedildi:", save_path)
            else:
                print("Görüntü Kaydedilmedi.")
                
    # process image file
    
    elif file_path.lower().endswith((".jpg", ".jpeg", ".png")):
        print("İşleniyor...")
        image = cv2.imread(file_path)
        processed_image = process_image(image)
        cv2.imshow("Mozaiklenmis Goruntu", processed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # save option
        
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg", 
                                                 filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if save_path:
            cv2.imwrite(save_path, processed_image)
            print("Görüntü Kaydedildi:", save_path)
        else:
            print("Görüntü Kaydedilmedi.")

if __name__ == "__main__":
    mozaic()
