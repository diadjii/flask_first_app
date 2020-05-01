from flask import Flask, render_template, request, url_for
from flask import send_file, flash, redirect
from werkzeug.utils  import secure_filename

import os

app = Flask(__name__)
app.secret_key = 'b\xab\xd5\xe6\x7f\xd0\x92q\xce\x91\xcd7E\xd2\xde\xeb\xb0\xdbY\x14&\xf9X\x14'

UPLOADED_DIR = './ups'

@app.route('/')
def index():
    return render_template('form.html.j2')


ALLOWEDS_FILES = {"png", "jpg", "jpeg"}

@app.route('/image/create', methods=['POST'])
def post_image():
    file = request.files['file']

    if file and file.filename.split(".")[1] in ALLOWEDS_FILES:
        file.save(UPLOADED_DIR+secure_filename(file.filename))

        return "Nom du fichier {}".format(file.filename)
    else:
        return "Veiller envoyer un image"

@app.route('/image/view')
def view_images():
    images = os.listdir(UPLOADED_DIR)

    return render_template("list_image.html.j2", images=images)

@app.route('/image/<name>')
def upped(name):
    if os.path.isfile(UPLOADED_DIR+'/'+name):
        return send_file(UPLOADED_DIR+'/'+name)
    else:
        flash("Cette image n'existe pas.")
        return redirect(url_for("view_images"))
if __name__ == '__main__':
    app.run(debug=True)
