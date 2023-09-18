import os
import tempfile

from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from ch.ehi.basics.settings import Settings
from org.interlis2.validator import Validator

UPLOAD_FOLDER = '/tmp'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        temp_dir = tempfile.mkdtemp()
        log_file = os.path.join(temp_dir, "mylog.log")
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

