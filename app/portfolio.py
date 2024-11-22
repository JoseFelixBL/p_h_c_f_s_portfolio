from flask import (
    Blueprint, render_template
)

# Definimos nuestro Blueprint con nombre portfolio, __name__, y el prefijo de ruta
bp = Blueprint('portfolio', __name__, url_prefix='/')

# Defino mi primera ruta


@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html')


@bp.route('/mail', methods=['POST'])
def mail():
    return render_template('portfolio/sent_mail.html')
