from flask import (
    Blueprint, render_template, request, redirect, url_for, current_app
)
# import sendgrid
# from sendgrid.helpers.mail import *
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Definimos nuestro Blueprint con nombre portfolio, __name__, y el prefijo de ruta
bp = Blueprint('portfolio', __name__, url_prefix='/')

# Defino mi primera ruta


@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html')


@bp.route('/mail', methods=['GET', 'POST'])
def mail():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        send_email(name, email, message)
        return render_template('portfolio/sent_mail.html')

    return redirect(url_for('portfolio.index'))


def send_email(name, email, message):
    mi_email = 'jfbello.adds@gmail.com'
    # sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])

    if True:
        contenido = f"""
            <p>Hola José:<br>Tienes un nuevo contacto desde la web:</p>
            <p>Nombre: {name}</p>
            <p>Correo: {email}</p>
            <p>Mensaje: {message}</p>
        """
        message = Mail(
            from_email='jfbello.adds@gmail.com',
            to_emails='jfbello.work@gmail.com',
            subject='Sending with Twilio SendGrid is Fun',
            html_content=contenido
        )
        # '<strong>and easy to do anywhere, even with Python</strong>'
        try:
            # sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            sg = SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
    else:
        # Esto es cómo lo dijo en el vídeo pero no me funciona
        from_email = Email(mi_email)
        to_email = To(mi_email, substitutions={
            '-name-': name,
            '-email-': email,
            '-message-': message
        })

        html_content = """
            <p>Hola José; tienes un nuevo contacto desde la web:</p>
            <p>Nombre: -name-</p>
            <p>Correo: -email-</p>
            <p>Mensaje: --message-</p>
        """
        mail = Mail(mi_email, to_email, 'Nuevo contacto desde la web',
                    html_content=html_content)
        response = sg.client.mail.send.post(request_body=mail.get())
