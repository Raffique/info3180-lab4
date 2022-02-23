from flask_wtf import FlaskForm
from wtforms import FileField
from flask_wtf.file import FileRequired, FileAllowed

image_types = ['jpg', 'png', 'jpeg', 'gif', 'svg', 'webp']

class UploadForm(FlaskForm):
    file = FileField('File', validators=[FileAllowed(image_types, 'Image only!'), FileRequired('File was empty!')])