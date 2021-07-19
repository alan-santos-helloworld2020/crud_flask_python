from flask import Flask,render_template,redirect,request
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
import json;



app  = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco/onload.db'
db = SQLAlchemy(app)

"""criação do banco e tabelas"""

class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String,nullable=False)
    telefone = db.Column(db.String,nullable=False)
    email = db.Column(db.String,nullable=False)
    cep = db.Column(db.String,nullable=False)

db.create_all()

"""criação de filtros"""
@app.template_filter('forjson')
def to_json(obj):
    return json.dumps(obj)



"""criação das rotas"""

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/salvar',methods=['GET','POST'])
def salvar():
    cl = Clientes(nome=request.form['nome'],
    telefone=request.form['telefone'],
    email=request.form['email'],
    cep=request.form['cep']
    )
    db.session.add(cl)
    db.session.commit()
    db.session.close()
    return redirect(url_for('clientes'))


@app.route('/clientes')
def clientes():
    return render_template('clientes.html',clientes = Clientes.query.all())


@app.route('/editar',methods=['GET','POST'])
def editar():
    id = request.form['id_cliente']
    cl =Clientes.query.filter_by(id=id).first()
  
    cl.nome = request.form['nome']
    cl.telefone=request.form['telefone']
    cl.email=request.form['email']
    cl.cep=request.form['cep']

    db.session.add(cl)
    db.session.commit()
    db.session.close()
    return render_template('clientes.html',clientes = Clientes.query.all())
    

@app.route('/deletar/<id>')
def deletar(id):
    Clientes.query.filter_by(id=id).delete()
    db.session.commit()
    db.session.close()
    return redirect(url_for('clientes'))


app.run(debug=True)












