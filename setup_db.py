from app import create_app, db
from app.models import Usuario

app = create_app()

with app.app_context():
    novo_usuario = Usuario(nome="Wallison", email="wallison@email.com")
    novo_usuario.set_senha("1234")  # Criptografa a senha corretamente
    
    db.session.add(novo_usuario)
    db.session.commit()
    
    print("Usuário adicionado com sucesso! ✅")
