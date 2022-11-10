import os
from flask import Flask, render_template, request, send_from_directory, send_file, url_for, redirect
from flask_dropzone import Dropzone
from attendance import att, intoDB, download_csvs, removeFiles
import response

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    DROPZONE_MAX_FILE_SIZE=1024,
    DROPZONE_TIMEOUT=5*60*1000)

dropzone = Dropzone(app)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        if request.form.get('upload') == 'Upload':
            return render_template('/upload.html')
        if request.form.get('sftp') == 'SFTP':
            removeFiles()
            download_csvs()
            att()
            intoDB()
            with open("output.csv", encoding="utf8") as file:
                return render_template("/csv_table.html", csv=file)
    return render_template('index.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        if request.form.get('action1') == 'Submit':
            ret = att()
            intoDB()
            with open("output.csv", encoding="utf8") as file:
                return render_template("/csv_table.html", csv=file)
        else:
            f = request.files.get('file')
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))

    return render_template('upload.html')


@app.route('/csv_table', methods=['POST', 'GET'])
def csv_table():
    if request.method == 'POST':
        if request.form.get('action') == 'Download':
            download = send_file('output.csv')
            return download


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
