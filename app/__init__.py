from flask import Flask
import os
from dotenv import load_dotenv


def create_app():
    """Creamos nuestra aplicación Flask y le incorporamos los Blueprint necesarios"""
    app = Flask(__name__)

    load_dotenv()

    # Usamos/Cogemos las configuraciónes de esta aplicación
    app.config.from_mapping(
        SENDGRID_KEY=os.environ.get('SENDGRID_KEY'),
    )

    # Importamos el archivo con la lógica de nuestro portafolio
    from . import portfolio

    # Registramos el Blueprint, es decir, creamos un módulo de esto
    app.register_blueprint(portfolio.bp)

    return app
