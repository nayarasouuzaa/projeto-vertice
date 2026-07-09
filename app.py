from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do Banco de Dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vertice.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definição do Modelo do Banco de Dados para a Comunidade
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Post {self.id} de {self.usuario}>'


# Rota Principal - Carrega a página e busca os posts do banco
@app.route('/')
def index():
    # Busca todos os posts salvos, do mais recente para o mais antigo
    posts = Post.query.order_by(Post.data.desc()).all()
    return render_template('index.html', posts=posts)


# Rota para Processar o Formulário de Feedback
@app.route('/comunidade/postar', methods=['POST'])
def postar_feedback():
    usuario = request.form.get('usuario')
    conteudo = request.form.get('conteudo')

    if usuario and conteudo:
        # Cria um novo registro com o que veio do formulário
        novo_post = Post(usuario=usuario, conteudo=conteudo)
        db.session.add(novo_post)
        db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    # Cria o banco de dados e as tabelas caso não existam dentro do contexto do app
    with app.app_context():
        db.create_all()
    app.run(debug=True)