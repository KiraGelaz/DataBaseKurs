from flask import Blueprint, request, render_template
from flask_login import login_required

from ..extentions import db
from ..models.auto_personnel import Auto_personnel


auto_personnel = Blueprint('auto_personnel', __name__)


@auto_personnel.route('/auto_personnel')
@login_required
def auto_personnel_table():
    persons = Auto_personnel.query.all()
    return render_template('auto_personnel/tableperson.html', persons=persons)


@auto_personnel.route('/auto_personnel/createperson', methods=['POST', 'GET'])
@login_required
def createperson():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        father_name = request.form.get('father_name')

        auto_personnel = Auto_personnel(first_name=first_name, last_name=last_name, father_name=father_name)

        try:
            db.session.add(auto_personnel)
            db.session.commit()
            persons = Auto_personnel.query.all()
            return render_template('auto_personnel/tableperson.html', persons=persons)
        except Exception as e:
            print(str(e))
            return render_template('auto_personnel/createperson.html')
    else:
        return render_template('auto_personnel/createperson.html')


@auto_personnel.route('/auto_personnel/<int:id>/changeperson', methods=['POST', 'GET'])
@login_required
def changeperson(id):
    person = Auto_personnel.query.get(id)
    if request.method == 'POST':
        person.first_name = request.form.get('first_name')
        person.last_name = request.form.get('last_name')
        person.father_name = request.form.get('father_name')

        try:
            db.session.commit()
            persons = Auto_personnel.query.all()
            return render_template('auto_personnel/tableperson.html', persons=persons)
        except Exception as e:
            print(str(e))
            return render_template('auto_personnel/changeperson.html', person=person)
    else:
        return render_template('auto_personnel/changeperson.html', person=person)


@auto_personnel.route('/auto_personnel/<int:id>/deleteperson', methods=['POST', 'GET'])
@login_required
def deleteperson(id):
    person = Auto_personnel.query.get(id)
    if request.method == 'POST':
        try:
            db.session.delete(person)
            db.session.commit()
            persons = Auto_personnel.query.all()
            return render_template('auto_personnel/tableperson.html', persons=persons)
        except Exception as e:
            print(str(e))
            return render_template('auto_personnel/deleteperson.html', person=person)
    else:
        return render_template('auto_personnel/deleteperson.html', person=person)
