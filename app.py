#!/home/irtza/Downloads/enter/pkgs/flask-0.10.1-py27_1/lib/python2.7
##!flask/bin/python
import os
from flask import Flask , request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

UPLOAD_FOLDER = '/home/irtza/deepAlpr/deep-Alpr-api/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#maximum 16mb upload allowed!
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Utility functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <h3>TESTING FILE UPLOAD </h3>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>'''

#This method returns what happens after the file is uploaded
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
    #This is sent when BASE URL recieves a POST or GET

if __name__ == '__main__':
    app.run(debug=True)