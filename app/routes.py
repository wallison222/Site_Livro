from flask import Blueprint, render_template, redirect, url_for, flash
from .models import db, Usuario


main = Blueprint("main", __name__)  # Definindo o Blueprint corretamente


from flask import send_from_directory

from flask import send_from_directory

@main.route('/')
def home():
    return render_template('index.html')  # Certifique-se de que o arquivo existe em `templates`

@main.route('/inicio')
def inicio():
    return send_from_directory('static/pdf', 'Reencontro_Amoroso.pdf')




