from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os

# this creates the Flask app
app = Flask(__name__)

# these are used to configure the app 
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'


# this creates a class called UploadFileForm, which
# inherits everythig from FlaskForm.
# inside the form, there will be two components:
# 1. a FileField named 'File', and
# 2. a SubmitField named 'Upload File'

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Upload File")


# this routes traffic to different places in our web folder.
# both http://website.com and http://website.com/home will redirect to here.

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])


# this is a function called 'home'. 
# Using Flask's render_template, it will return the index.html file from the templates folder.
# When this page loads, it will:
# 1. create an instance of class UploadFileForm (which creates instances of file and submit) and call it 'form',
# 2. grab the file 'index.html', and create an instance of 'form' and assignit to the argument form,
# 3. and pass those 2 things into the render_template() function  

def home():
    form  = UploadFileForm()

    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        return "File has been uploaded"




    return render_template('index.html', form=form)


# this will launch the Flask  app
if __name__ == '__main__':
    app.run(debug=True)
