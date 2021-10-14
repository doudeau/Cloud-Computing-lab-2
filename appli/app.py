import os
from flask import Flask, render_template, request, redirect, send_file
from bucket import upload_file, show_image
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "lab2-doggy-doggo"

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
        upload_file(f"uploads/{f.filename}", BUCKET)
        return redirect("/")

@app.route("/pics")
def list():
    contents = show_image(BUCKET)
    return render_template('collection.html', contents=contents)
