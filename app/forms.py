from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired ,Length



class AddForm(FlaskForm):      # entering contact details
    name = StringField('Name', validators=[DataRequired()])
    add= SubmitField('Submit')

class UploadTestResult(FlaskForm):  # uploading test result
    name= StringField('Name', validators=[DataRequired()])
    test_result= StringField('Test Result', validators=[DataRequired()])
    add= SubmitField('Upload Test Result')
