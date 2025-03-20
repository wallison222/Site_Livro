from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import CadastroForm, LoginForm
from app.models import db, Usuario  # Apenas importação de `db` e `Usuario`

main = Blueprint("main", __name__)  # Definindo o Blueprint corretamente

@main.route("/")
def index():
    try:
        usuarios = Usuario.query.all()  # Tenta buscar os usuários no banco
    except Exception as e:
        flash(f"Erro ao carregar usuários: {str(e)}", "danger")
        usuarios = []  # Se der erro, a lista fica vazia para evitar problemas
    
    return render_template('index.html', usuarios=usuarios)

@main.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        usuario_existente = Usuario.query.filter_by(email=form.email.data).first()
        if usuario_existente:
            flash('Email já cadastrado. Tente outro.', 'danger')
            return redirect(url_for('main.cadastro'))

        novo_usuario = Usuario(nome=form.nome.data, email=form.email.data)
        novo_usuario.set_senha(form.senha.data)
        db.session.add(novo_usuario)
        db.session.commit()

        flash('Usuário cadastrado com sucesso!', 'success')
        return redirect(url_for('main.login'))
    
    return render_template('cadastro.html', form=form)



from flask import send_from_directory

from flask import send_from_directory

@main.route('/inicio')
def inicio():
    return send_from_directory('static/pdf', 'Reencontro_Amoroso.pdf')




@main.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        
        if usuario and usuario.verificar_senha(form.senha.data):
            flash(f'Login realizado com sucesso, {usuario.nome}!', 'success')
            return redirect(url_for('main.index'))  # Vai para a página inicial após login
        
        flash('E-mail ou senha inválidos. Tente novamente.', 'danger')
    
    return render_template('login.html', form=form)

