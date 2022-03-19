import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

# pip install flask-sqlalchemy  
from flask_sqlalchemy import SQLAlchemy

# caminho onde está o projeto, em seguida, configuramos um arquivo de banco de dados  
# com o caminho completo informando ao SQLAlchemy qual mecanismo estamos utilizando
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "seriadodatabase.db"))

# informamos à nossa aplicação onde nosso banco de dados será armazenado
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# inicializamos uma conexão com o banco de dados e mantemos isso na db variável, 
# isso faz a interação da aplicação com o banco de dados
db = SQLAlchemy(app)

# classe que herda de um modelo básico de banco de dados
class Seriado(db.Model):
    titulo = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Titulo: {}>".format(self.titulo)


# criação e armazenamento de seriados
@app.route("/", methods=["GET", "POST"])
def home():
    seriados = None
    if request.form:
        try:
            seriado = Seriado(titulo=request.form.get("titulo"))
            db.session.add(seriado)
            db.session.commit()
        except Exception as e:
            print("Falha ao adicionar o seriado")
            print(e)
    seriados = Seriado.query.all() # recuperando seriados do nosso banco de dados
    return render_template("home.html", seriados=seriados)

# atualização de seriados
@app.route("/atualizar", methods=["POST"])
def atualizar():
    try:
        novoTitulo = request.form.get("novoTitulo")
        velhoTitulo = request.form.get("velhoTitulo")
        seriado = Seriado.query.filter_by(titulo=velhoTitulo).first()
        seriado.titulo = novoTitulo
        db.session.commit()
    except Exception as e:
        print("Não foi possível atualizar o seriado")
        print(e)
    return redirect("/")

# deletar seriados
@app.route("/deletar", methods=["POST"])
def deletar():
    titulo = request.form.get("titulo")
    seriado = Seriado.query.filter_by(titulo=titulo).first()
    db.session.delete(seriado)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    db.create_all() # inicializando nosso banco de dados
    app.run(host='0.0.0.0', port=8087, debug=True)


    
