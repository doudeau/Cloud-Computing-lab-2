import os
from flask import Flask, render_template, request, redirect, send_file
from bucket import upload_file, show_image, choose4
from werkzeug.utils import secure_filename
import sys

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "lab2-doggy-doggo"

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def list():
    contents = choose4(show_image(BUCKET))
    return render_template('collection.html', contents=contents)

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
        upload_file(f"uploads/{f.filename}", BUCKET)
        return redirect("/")

@app.route("/pics", methods=['GET','POST'])
def list():
    contents,indices = choose4(show_image(BUCKET))
    print(indices)
    return render_template('collection.html', contents=contents)

@app.route("/result/", methods=['POST'])
def saveResult():
    select = request.form.getlist("choice")
    return(str(select))
    #print('Hello world!')
    #return render_template('response.html')

