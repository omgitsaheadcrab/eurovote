from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from eurovote import db
from eurovote.models import Vote, User
from eurovote.votes.forms import VoteForm

votes = Blueprint('votes', __name__)

@votes.route('/vote',methods=['GET','POST']) 
def cast():
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))
    form = VoteForm()
    if form.validate_on_submit():
        cvote = Vote(name=form.name.data,
                     song=form.song.data,
                     outfit=form.outfit.data,
                     performance=form.performance.data,
                     user_id=current_user.id)
        db.session.add(cvote)
        db.session.commit()
        flash('Your vote has been cast.','success')
        return redirect(url_for('votes.cast'))
    return render_template('vote.html', title='Vote', form=form)


