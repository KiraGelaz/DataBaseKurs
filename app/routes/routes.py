from flask import Blueprint, request, render_template
from flask_login import login_required

from ..extentions import db
from ..models.routes import Routes

routes = Blueprint('routes', __name__)


@routes.route('/routes')
@login_required
def routes_table():
    routes = Routes.query.all()
    return render_template('routes/tableroutes.html', routes=routes)


@routes.route('/routes/createroutes', methods=['POST', 'GET'])
@login_required
def createroutes():
    if request.method == 'POST':
        name = request.form.get('name')
        route = Routes(name=name)

        try:
            db.session.add(route)
            db.session.commit()
            routes = Routes.query.all()
            return render_template('routes/tableroutes.html', routes=routes)
        except Exception as e:
            print(str(e))
            return render_template('routes/createroutes.html')
    else:
        return render_template('routes/createroutes.html')


@routes.route('/routes/<int:id>/changeroutes', methods=['POST', 'GET'])
@login_required
def changeroutes(id):
    route = Routes.query.get(id)
    if request.method == 'POST':
        route.name = request.form.get('name')
        try:
            db.session.commit()
            routes = Routes.query.all()
            return render_template('routes/tableroutes.html', routes=routes)
        except Exception as e:
            print(str(e))
            return render_template('routes/changeroutes.html', route=route)
    else:
        return render_template('routes/changeroutes.html', route=route)


@routes.route('/routes/<int:id>/deleteroutes', methods=['POST', 'GET'])
@login_required
def deleteroutes(id):
    route = Routes.query.get(id)
    if request.method == 'POST':
        try:
            db.session.delete(route)
            db.session.commit()
            routes = Routes.query.all()
            return render_template('routes/tableroutes.html', routes=routes)
        except Exception as e:
            print(str(e))
            return render_template('routes/deleteroutes.html', route=route)
    else:
        return render_template('routes/deleteroutes.html', route=route)
