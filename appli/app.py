import os
from flask import Flask, render_template, request, redirect, send_file
from bucket import upload_file, show_image, choose4, getListPics,getIdList
from dico import response,creationRes
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "lab2-doggy-doggo"

listId = 0

if __name__ == '__main__':
    app.run(debug=True)

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
        upload_file(f"uploads/{f.filename}", BUCKET)
        return redirect("/")

@app.route("/", methods=['GET','POST'])
def list():
    contents, indices = choose4(show_image(BUCKET))
    print(indices)
    listPics = getListPics(BUCKET)
    global listId 
    listId = getIdList(listPics,indices)
    return render_template('collection.html', contents=contents)

@app.route("/result/", methods=['POST'])
def saveResult():
    if request.method =='POST':
        select = request.form.getlist("choice")
        f = response(creationRes(select,listId))
        with open('result.json', 'w') as fp:
            json.dump(f, fp)
        upload_file("result.json", BUCKET)

    return render_template('response.html')

