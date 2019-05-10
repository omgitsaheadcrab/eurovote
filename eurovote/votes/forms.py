from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired

COUNTRY_CHOICES = [('Spain','Spain'), ('Cyprus','Cyprus'), ('Germany','Germany')]
SCORES = [(0,'0'),(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')]

class VoteForm(FlaskForm):
   name = SelectField(label='Country', choices=COUNTRY_CHOICES)
   song = RadioField('Song', coerce=int, choices=SCORES)
   outfit = RadioField('Outfit', coerce=int, choices=SCORES)
   performance = RadioField('Performance', coerce=int, choices=SCORES)
   
   submit = SubmitField('Submit')
