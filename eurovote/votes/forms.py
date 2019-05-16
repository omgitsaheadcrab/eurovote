from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, InputRequired

COUNTRY_CHOICES = [('Ukraine','Ukraine'),
                   ('Spain','Spain'),
                   ('Slovenia','Slovenia'),
                   ('Lithuania','Lithuania'),
                   ('Austria','Austria'),
                   ('Estonia','Estonia'),
                   ('Norway','Norway'),
                   ('Portugal','Portugal'),
                   ('United Kingdom','United Kingdom'),
                   ('Greece','Greece'),
                   ('Germany','Germany'),
                   ('Albania','Albania'),
                   ('France','France'),
                   ('Czech Republic','Czech Republic'),
                   ('Denmark','Denmark'),
                   ('Australia','Australia'),
                   ('Finland','Finland'),
                   ('Bulgaria','Bulgaria'),
                   ('Moldova','Moldova'),
                   ('Sweden','Sweden'),
                   ('Hungary','Hungary'),
                   ('Israel','Israel'),
                   ('Netherlands','Netherlands'),
                   ('Ireland','Ireland'),
                   ('Cyprus','Cyprus'),
                   ('Italy','Italy')]

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

