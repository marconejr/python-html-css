import sqlite3  # importando o SQLite
from flask import Flask, request, session, g, redirect, abort, render_template, flash #importanto módulos

# CONFIGURAÇÃO
DATABASE = "blog.db" #banco
SECRET_KEY = 'pudim' #senha

app = Flask(__name__) # variavel do python que guarda o nome do arquivo a ser executado, só essa linha ela cria uma aplicação mínima
app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def antes_requisicao():
    g.bd=conectar_bd()

@app.teardown_request
def depois_request(exc):
    g.bd.close()

@app.route('/')
def exibir_entradas():
    return render_template('exibir_entradas.html')


@app.route('/hello') # é  decorators, onde é passado string que será uma URL, faz um link entre a url e extensão
def pagina_inicial():
    return "Hello World"



