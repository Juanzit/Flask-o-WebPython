# -----------=---------------
# Ir no cmd e digitar:
# pip install Flask
# -----------=---------------
from flask import Flask, render_template, request, jsonify, url_for, redirect

# Iniciando site
app = Flask(
    __name__, template_folder='C:\Projetos\Roadmap Python\Flask Python web\Templates')

# Definindo o link da pagina
# decorator = antes da definição da função, atribui uma nova funcionalidade para a função
# Essa função vai ser exibida na pagina principal do site

# eu edito o site de acordo com as normas do html e css

# Criando uma função com o que quero exibir na página retornando o arquivo html


@app.route("/contatos")
def contatos():
    return render_template("Contatos.html", empresa="Roadmappython")
# Um exemplo de uma página em que pelo código eu levo uma variável para o arquivo.html

# Redireciona para a função desejada ex:contatos


@app.route("/admin")
def admin():
    return redirect(url_for("contatos"))

# passando o que o usuário digitou em uma pagina , para outra pagina


@app.route('/', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        user = request.form.get('nome')
        email = request.form.get('email')
        return redirect(url_for('usuario', email=email, user=user))
    return render_template('Paginicial.html')


@app.route('/usuarios/<user>')
def usuario(user):
    nome = user
    email = request.args.get('email', None)
    return render_template('usuarios.html', nome=nome, email=email)


# qualquer nome que for digitado no lugar de <usuario> exibirá uma pagina com tal nome
"""
@app.route("/usuarios/<usuario>")
def usuarios(usuario):
   # a primeira variavel se refere a do arquivo.html e a segunda é a do código
    return render_template("usuarios.html", usuario=usuario)

# Qualquer outra coisa que for digitada na frente da barra aparecerá uma mensagem de erro
"""


@app.route("/<string:palavra>")
def erro(palavra):
    return "Error 404 Página {} não encontrada".format(palavra)


# Colocar o site no ar
# Se o arquivo for executado diretamente pelo arquivo o if vai rodar
# Futuramente pode dar erro se nao tiver o if
if __name__ == '__main__':
    app.run(debug=True)

# debug=True , ele vai atualizando as informações no site
