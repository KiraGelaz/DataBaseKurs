from flask import Blueprint, request, render_template
from flask_login import login_required

from ..models.auto import Auto
from ..models.routes import Routes
from ..extentions import db
from ..models.journal import Journal

journal = Blueprint('journal', __name__)


@journal.route('/journal')
@login_required
def journal_table():
    journals = Journal.query.all()
    return render_template('journal/tablejournal.html', journals=journals)


@journal.route('/journal/createjournal', methods=['POST', 'GET'])
@login_required
def createjournal():
    routes = Routes.query.all()
    autos = Auto.query.all()
    if request.method == 'POST':
        time_out = request.form.get('time_out')
        time_in = request.form.get('time_in')
        route_id = request.form.get('route_id')
        auto_id = request.form.get('auto_id')

        journal = Journal(time_out=time_out, time_in=time_in, route_id=route_id, auto_id=auto_id)

        try:
            db.session.add(journal)
            db.session.commit()
            journals = Journal.query.all()
            return render_template('journal/tablejournal.html', journals=journals)
        except Exception as e:
            print(str(e))
            return render_template('journal/createjournal.html', routes=routes, autos=autos)
    else:
        return render_template('journal/createjournal.html', routes=routes, autos=autos)


@journal.route('/journal/<int:id>/changejournal', methods=['POST', 'GET'])
@login_required
def changejournal(id):
    routes = Routes.query.all()
    autos = Auto.query.all()
    journal = Journal.query.get(id)
    if request.method == 'POST':
        journal.time_out = request.form.get('time_out')
        journal.time_in = request.form.get('time_in')
        journal.route_id = request.form.get('route_id')
        journal.auto_id = request.form.get('auto_id')

        try:
            db.session.commit()
            journals = Journal.query.all()
            return render_template('journal/tablejournal.html', journals=journals)
        except Exception as e:
            print(str(e))
            return render_template('journal/changejournal.html', journal=journal, routes=routes, autos=autos)
    else:
        return render_template('journal/changejournal.html', journal=journal, routes=routes, autos=autos)


@journal.route('/journal/<int:id>/deletejournal', methods=['POST', 'GET'])
@login_required
def deletejournal(id):
    journal = Journal.query.get(id)
    if request.method == 'POST':
        try:
            db.session.delete(journal)
            db.session.commit()
            journals = Journal.query.all()
            return render_template('journal/tablejournal.html', journals=journals)
        except Exception as e:
            print(str(e))
            return render_template('journal/deletejournal.html', journal=journal)
    else:
        return render_template('journal/deletejournal.html', journal=journal)
