##!flask/bin/python

#
# ===========Guidelines for Usama================
#	comment one # from first line if you are to run it as executable i.e ./app.py
#   otherwise python app.py should be fine.
#	JSON file is just dumped there from ... http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
#	Image upload works fine, check the myclassify() function it is the view function
#	I left work incomplete. Pull request me on this one... 


import os
from flask import Flask , jsonify, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

UPLOAD_FOLDER = '/home/irtza/deepAlpr/deep-Alpr-api/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#JSON
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

# Utility functions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
def my_classify(uploadfolder, filename):
	'''
	this is called a View function in FLASK terminology
	it must return something
	'''
	return "hello"

@app.route('/', methods=['GET', 'POST'])
def welcome():
	return "welcome to deepAlpr API landing page"

@app.route('/deepAlpr/api/v1.0', methods=['GET', 'POST'])
def upload_file():
    '''
    Possible Exposing of Classify method here?????
    request method is POST.. so send image here.
    notice ELSE part sends the form with action POST.
    '''
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return my_classify(app.config['UPLOAD_FOLDER'] , filename)
            #return redirect(url_for('uploaded_file',filename=filename))
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
@app.route('/deepAlpr/api/v1.0/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
    #This is sent when BASE URL recieves a POST or GET

if __name__ == '__main__':
    app.run(debug=True)