from flask import Blueprint, request, render_template
from flask_login import login_required

from ..models.auto_personnel import Auto_personnel
from ..extentions import db
from ..models.auto import Auto

auto = Blueprint('auto', __name__)


@auto.route('/auto')
@login_required
def auto_table():
    autos = Auto.query.all()
    return render_template('auto/tableauto.html', autos=autos)


@auto.route('/auto/createauto', methods=['POST', 'GET'])
@login_required
def createauto():
    persons = Auto_personnel.query.all()
    if request.method == 'POST':
        num = request.form.get('num')
        color = request.form.get('color')
        mark = request.form.get('mark')
        personal_id = request.form.get('personal_id')

        auto = Auto(num=num, color=color, mark=mark, personal_id=personal_id)

        try:
            db.session.add(auto)
            db.session.commit()
            autos = Auto.query.all()
            return render_template('auto/tableauto.html', autos=autos)
        except Exception as e:
            print(str(e))
            return render_template('auto/createauto.html', persons=persons)
    else:
        return render_template('auto/createauto.html', persons=persons)


@auto.route('/auto/<int:id>/changeauto', methods=['POST', 'GET'])
@login_required
def changeauto(id):
    persons = Auto_personnel.query.all()
    auto = Auto.query.get(id)
    if request.method == 'POST':
        auto.num = request.form.get('num')
        auto.color = request.form.get('color')
        auto.mark = request.form.get('mark')
        auto.personal_id = request.form.get('personal_id')

        try:
            db.session.commit()
            autos = Auto.query.all()
            return render_template('auto/tableauto.html', autos=autos)
        except Exception as e:
            print(str(e))
            return render_template('auto/changeauto.html', auto=auto, persons=persons)
    else:
        return render_template('auto/changeauto.html', auto=auto, persons=persons)


@auto.route('/auto/<int:id>/deleteauto', methods=['POST', 'GET'])
@login_required
def deleteauto(id):
    auto = Auto.query.get(id)
    if request.method == 'POST':
        try:
            db.session.delete(auto)
            db.session.commit()
            autos = Auto.query.all()
            return render_template('auto/tableauto.html', autos=autos)
        except Exception as e:
            print(str(e))
            return render_template('auto/deleteauto.html', auto=auto)
    else:
        return render_template('auto/deleteauto.html', auto=auto)
