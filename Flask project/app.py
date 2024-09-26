from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from PIL import Image
import pytesseract
import io

app = Flask(__name__)
CORS(app)

# Serve the HTML file
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract_text():
    file = request.files['image']
    image = Image.open(file.stream)
    text = pytesseract.image_to_string(image, lang='eng+hin')
    return jsonify({"extracted_text": text})

if __name__ == '__main__':
    app.run(debug=True)
