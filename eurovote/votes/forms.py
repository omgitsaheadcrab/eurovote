from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, RadioField
from wtforms.validators import DataRequired

class VoteForm(FlaskForm):
   song = RadioField('Song', coerce=int,
                     choices=[(0,'0'),(1,'1'),(2,'2'),
                              (3,'3'),(4,'4'),(5,'5')])
   outfit = RadioField('Outfit', coerce=int,
                       choices=[(0,'0'),(1,'1'),(2,'2'),
                                (3,'3'),(4,'4'),(5,'5')])
   performance = RadioField('Performance', coerce=int,
                            choices=[(0,'0'),(1,'1'),(2,'2'),
                                     (3,'3'),(4,'4'),(5,'5')])
   
   submit = SubmitField('Submit')
