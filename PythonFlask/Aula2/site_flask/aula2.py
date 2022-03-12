from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/paginaInicial")
def pgInicial():
    return "Consegui começar a fazer minha primeira aplicação web"

@app.route("/erro")
def erro():
   return "Página não encontrada" 

if(__name__ == "__main__"):
    app.run()

