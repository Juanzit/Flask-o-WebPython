# Flask-o-WebPython
## Criando um website em python usando Flask

----------------------------------------------=--------------------------------------------------------<br>
Flask é  um micro-framework,utilizado para criar APIS e sistemas mais simples , diferente do django que é mais complexo porém é mais completo , no Flask você faz cada etapa e entende o processo<br>
----------------------------------------------=---------------------------------------------------------<br>
começamos com a instalação da biblioteca que iremos utilizar<br>
--> Winndows+R <br>
--> CMD <br>
--> pip install Flask <br>
    ou <br>
--> pip3 install Flask <br>
-------------------------=-------------------------------
Primeiro importemos as bibliotecas que serão utilizadas:
```
from flask import Flask, render_template, url_for, redirect, request
```

Para iniciar o site colocamos deste modo, seguindo o que a documentação do Flask pede de padrao
app = Flask(__name__)
-------------------------=-------------------------------
Após a instalação do Heroku criamos um arquivo de texto chamado **profile** sem extensão,no mesmo local em que está o código
Dentro do arquivo se coloca:
```
web: guinicorn nome do arquivo : nome do site
```
```
Ex  web: guinicorn Flask:roadmappython
```
Agora que ja criamos o procfile iremos criar o requirements.txt
```
pip freeze > requirements.txt
```
É criada uma lista de tudo que foi instalado e armazena tudo nesse arquivo.txt


-> Abrindo o CMD <-
_Não esqueça de abrir o cmd diretamente na pasta do projeto_
Exemplo C:\Projetos\Roadmap Python\Flask Python web

Iremos fazer login na sua conta do Heroku pelo terminal
```
Heroku login
```

inicie o Git para seguir com os procedimentos
```
Git init
```
O Heroku necessita do Git com a sua conta logada
Caso nao tenha cadastrado seu email e nick , siga os passos abaixo:
```
git config --global user.email "Seu email aqui"
```
```
git config --global user.name "Seu nome de usuário aqui"
```
