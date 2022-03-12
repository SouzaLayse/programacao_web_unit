from shutil import unregister_unpack_format
from flask import Flask, request, render_template, redirect, url_for

# request> pega as requisições do cliente e cria um objeto para facilitar o acesso dessas informações
# render_template > renderiza o template do html
# redirect > redirenciona para a página, ex.: usuario
# url_for > redireciona para a url esperada

app = Flask(__name__)

@app.route('/olamundo')
def hello():
    return "Olá"

@app.route('/mensagem/') # por padrão define /mensagem/ e tanto faz com ou sem / para o usuário pq vai conseguir encontrar a página
def mensagem():
    nome = 'Layse'
    return f'Olá {nome}!' # f -> formata a string

@app.route('/busca/')
def lerArgumentos():
    nome1 = request.args.get('nome')
    idade = request.args.get('idade')
    return f'Olá {nome1} você tem {idade} anos'

#pegando o exemplo de um site de vendas > magazineluiza
# <> pega o que o usuário digita
@app.route('/produtos/<produto>') 
def lerVariaveis(produto):
    return f'Você selecionou o produto {produto}'

@app.route('/valores/<int:valor>') # declarando que só vai receber um valor do tipo inteiro
def lerVariaveisInteiras(valor): 
    return f'O valor é {str(valor)}'

@app.route('/bemvindo/<nome>')
def retornarHTML(nome): 
    return f''' <h1> Olá {nome} </h1> '''    # html

# funcao para utilizar html
@app.route('/bemvindo/')
def retornarArquivoHtml():
    return render_template('bemvindo.html')

# seguindo a regra da função e do local ter o mesmo nome
# modificando para utilizar o usuario.html
@app.route('/admin/')
def admin():
    usuario = 'Admin' 
    # return 'Seja bem vindo Admin' # utilizado sem o usuario.html
    return render_template('usuario.html', usuario = usuario) # usuario = usuario para retornar a informação

@app.route('/aluno/')
def aluno():
    usuario = 'Aluno'
    # return 'Seja bem vindo Aluno' # utilizado sem o usuario.html
    return render_template('usuario.html', usuario = usuario) # usuario = usuario para retornar a informação

@app.route('/professor/')
def professor():
    usuario = 'Professor'
    # return 'Seja bem vindo Professor'  # utilizado sem o usuario.html
    return render_template('usuario.html', usuario = usuario) # usuario = usuario para retornar a informação

@app.route('/user/<tipo>') # é utilizado no usuario.html
def usuario(tipo):
    if tipo == 'aluno':
        return redirect(url_for('aluno'))
    elif tipo == 'professor':
        return redirect(url_for('professor'))
    elif tipo  == 'admin':
        return redirect(url_for('admin'))
    else:
        return '''<h1> Usuário não encontrado </h1>'''

@app.route('/usuarios/')  # passando a lista de usuários para o html
def lista_usuarios():
    lista_users = ['aluno', 'professor','admin']
    return render_template('usuarios.html', lista_users = lista_users)

# vai ser chamada quando o usuário digitar login ou quando clicar no botão
# será retornado apenas as informações da página
@app.route('/login/', methods=['GET', 'POST'])
def login():
    metodo = request.method
    if metodo == 'POST': # vai pegar a ação da página e fazer a verificação
        nome = request.form['nome'] 
        senha = request.form['senha']
        if nome == 'admin' and senha == 'admin':
            return "Seja bem vindo Admin"
        else:
            return "Informações incorretas. Verifique as informações!!"
    else: # carrega a página e pega as informações através do GET
        return render_template('login.html')

# página inicial
@app.route('/')
def index():
    return render_template('index.html')


if(__name__ == "__main__"):
    app.run(debug=True) # ir escrevendo a aplicação sem precisar pausar 
