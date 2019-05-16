from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from eurovote import db
from eurovote.models import Vote, User
from eurovote.votes.forms import VoteForm
from eurovote.votes.utils import Statistics, StatsTable
from sqlalchemy import desc, func
from sqlalchemy.sql import label

votes = Blueprint('votes', __name__)

@votes.route('/vote',methods=['GET','POST']) 
def cast():
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))

    form = VoteForm()

    # Search for all existing user votes, create list
    all_votes = Vote.query.filter_by(user_id=current_user.id).all()
    countries = []
    for vote in all_votes:
        countries.append(vote.name)

    # If existing vote, add tick
    keys = []
    vals = []
    for k,v in form.name.choices:
        keys.append(k)
        if v in countries:
            vals.append(v+'✓')
        else:
            vals.append(v)

    # Pass new choices to form
    choices_checked = list(zip(keys,vals))
    form.name.choices = choices_checked
    
    if form.validate_on_submit():
        # Current form submission
        cur = Vote.query.filter_by(user_id=current_user.id)\
                            .filter_by(name=form.name.data)\
                            .first()
        if cur:
            # Entry exists, update values
            current_user.votes[cur.id-1].song = form.song.data
            current_user.votes[cur.id-1].outfit = form.outfit.data
            current_user.votes[cur.id-1].performance = form.performance.data
            db.session.commit()
            if (form.name.data == 'Greece') or (form.name.data == 'Cyprus'):
                flash('Your vote has been updated. Ώπα!','success')
            else:
                flash('Your vote has been updated.','success')
            return redirect(url_for('votes.cast'))
        else:
            # No existing entry, add new
            cvote = Vote(name=form.name.data,
                         song=form.song.data,
                         outfit=form.outfit.data,
                         performance=form.performance.data,
                         user_id=current_user.id)
            db.session.add(cvote)
            db.session.commit()
            if (cvote.name == 'Greece') or (cvote.name == 'Cyprus'):
                flash('Your vote has been cast. Ώπα!','success')
            else:
                flash('Your vote has been cast.','success')
            return redirect(url_for('votes.cast'))
    return render_template('vote.html', title='Vote', form=form)


@votes.route('/stats',methods=['GET','POST']) 
def stat():
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))

    stat = Statistics()
    
    fields = ['song', 'outfit', 'performance']

    alltotals = db.session.query(Vote.name,
                                 label('total_score',
                                       func.sum(Vote.total_score(fields))),
                                 label('song_score',
                                       func.sum(Vote.total_score(['song']))),
                                 label('outfit_score',
                                       func.sum(Vote.total_score(['outfit']))),
                                 label('performance_score',
                                       func.sum(Vote.total_score(['performance']))),
    ).group_by('name').order_by(desc('total_score')).all()
    
    table = StatsTable(alltotals)
    
    total_score = db.session.query(Vote.name, label('total_score',func.sum(Vote.total_score(fields)))).group_by('name')
    
    stat.max_score = total_score.order_by(desc('total_score')).first()
    stat.min_score = total_score.order_by('total_score').first()

    total_song = db.session.query(Vote.name, label('total_score',func.sum(Vote.total_score(['song'])))).group_by('name')
    
    stat.max_song = total_song.order_by(desc('total_score')).first()
    stat.min_song = total_song.order_by('total_score').first()
    
    total_outfit = db.session.query(Vote.name, label('total_score',func.sum(Vote.total_score(['outfit'])))).group_by('name')
    
    stat.max_outfit = total_outfit.order_by(desc('total_score')).first()
    stat.min_outfit = total_outfit.order_by('total_score').first()

    total_perf = db.session.query(Vote.name, label('total_score',func.sum(Vote.total_score(['performance'])))).group_by('name')
    
    stat.max_performance = total_perf.order_by(desc('total_score')).first()
    stat.min_performance = total_perf.order_by('total_score').first()

    return render_template('stats.html', title='Statistics', stat=stat, table=table)
