from io import BytesIO

from flask import Blueprint, send_file
from flask_login import login_required
import pandas as pd

from ..extentions import db
from ..models.auto_personnel import Auto_personnel
from ..models.auto import Auto


excel = Blueprint('excel', __name__)


@excel.route('/download')
@login_required
def download():
    query = db.session.query(Auto, Auto_personnel).outerjoin(Auto_personnel, Auto.personal_id == Auto_personnel.id)
    results = query.all()

    data = []
    for auto, personnel in results:
        data.append({
            'Num': auto.num,
            'Color': auto.color,
            'Mark': auto.mark,
            'First Name': personnel.first_name if personnel else None,
            'Last Name': personnel.last_name if personnel else None,
            'Father Name': personnel.father_name if personnel else None,
        })

    df = pd.DataFrame(data)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Autos')
    output.seek(0)

    return send_file(output, download_name='database.xlsx', as_attachment=True)
