# app.py
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Mansi\AppData\Local\Programs\Tesseract\tesseract.exe'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        if file.filename == '':
            return 'No selected file'

        # Perform OCR
        extracted_text = ocr(file)

        return render_template('result.html', extracted_text=extracted_text)

    return render_template('upload.html')

def ocr(image):
    img = Image.open(image)
    text = pytesseract.image_to_string(img)
    return text

if __name__ == '__main__':
    app.run(debug=True)
