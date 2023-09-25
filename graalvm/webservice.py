import java
import os
import tempfile

from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

files = os.listdir(os.path.join(".venv", "javalib"))
for file in files:
    if file.endswith("jar"):
        #print(os.path.join(".venv", "javalib", file))
        java.add_to_classpath(os.path.join(".venv", "javalib", file))

Settings = java.type("ch.ehi.basics.settings.Settings")
Validator = java.type("org.interlis2.validator.Validator")

UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = {'xtf', 'xml', 'itf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            temp_dir = tempfile.TemporaryDirectory()
            log_file = os.path.join(temp_dir.name, "mylog.log")

            settings = Settings()
            settings.setValue(Validator.SETTING_LOGFILE, log_file)
            valid = Validator.runValidation([filepath], settings)

            with open(log_file,"r") as f:
                content = f.read()
                return content, 200, {'Content-Type': 'text/plain; charset=utf-8'}
            return "should not reach here"

    return '''
    <!doctype html>
    <title>Upload INTERLIS file</title>
    <h1>Upload INTERLIS file</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)





settings = Settings()
settings.setValue(Validator.SETTING_LOGFILE, "validation.log")
settings.setValue(Validator.SETTING_XTFLOG, "validation.log.xtf")

valid = Validator.runValidation(["ch.so.agi.av.inventar_kantonsgrenzzeichen.xtf"], settings)

print(valid)