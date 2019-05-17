from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, InputRequired

COUNTRY_CHOICES = [('Malta','Malta'),
                   ('Albania','Albania'),
                   ('Czech Republic','Czech Republic'),
                   ('Germany','Germany'),
                   ('Russia','Russia'),
                   ('Denmark','Denmark'),
                   ('San Marino','San Marino'),
                   ('North Macedonia','North Macedonia'),
                   ('Sweden','Sweden'),
                   ('Slovenia','Slovenia'),
                   ('Cyprus','Cyprus'),
                   ('Netherlands','Netherlands'),
                   ('Greece','Greece'),
                   ('Israel','Israel'),
                   ('Norway','Norway'),
                   ('United Kingdom','United Kingdom'),
                   ('Iceland','Iceland'),
                   ('Estonia','Estonia'),
                   ('Belarus','Belarus'),
                   ('Azerbaijan','Azerbaijan'),
                   ('France','France'),
                   ('Italy','Italy'),
                   ('Serbia','Serbia'),
                   ('Switzerland','Switzerland'),
                   ('Australia','Australia'),
                   ('Spain','Spain')]

SCORES = [(0,'0'),
          (1,'1'),
          (2,'2'),
          (3,'3'),
          (4,'4'),
          (5,'5')]

class VoteForm(FlaskForm):
   name = SelectField(label='Country', choices=COUNTRY_CHOICES,validators=[InputRequired()])
   song = RadioField('Song', coerce=int, choices=SCORES,validators=[InputRequired()])
   outfit = RadioField('Outfit', coerce=int, choices=SCORES,validators=[InputRequired()])
   performance = RadioField('Performance', coerce=int, choices=SCORES,validators=[InputRequired()])
   
   submit = SubmitField('Submit')

