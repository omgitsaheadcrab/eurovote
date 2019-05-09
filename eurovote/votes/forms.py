from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class VoteForm(FlaskForm):
   song = IntegerField('Song', validators=[DataRequired()])
   outfit = IntegerField('Outfit', validators=[DataRequired()])
   performance = IntegerField('Performance', validators=[DataRequired()])
   submit = SubmitField('Submit')
