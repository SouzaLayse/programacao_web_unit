from flask import Flask, render_template, request
import random

app = Flask(__name__)

#@app.route("/")
#def oiMundo():
#    return "Oi Mundo!"

@app.route("/", methods=["GET", "POST"])
def index():
    variavel = "Adivinhe o número correto"

    if request.method == "GET":
        return render_template("index.html", variavel=variavel)
    else:
        numero = random.randint(1,5)
        palpite = request.form.get(numero)

        if numero == palpite:
            return '<h1> Você acertou o número <h1>'
        else:
            return '<h1> Você não encontrou o número <h1>'

#@app.route('/<string:nome>')
#def error():
#    variavel = f'Error 404 - Página não encontrada)'
#    return render_template("error.html", variavel=variavel)

if(__name__ == "__main__"):
    app.run()

    



    
