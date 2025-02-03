
from flask import Flask, render_template, request
#from flask_wtf.csrf import CSRFProtect
import sqlite3

app = Flask(__name__)
#csrf = CSRFProtect(app)

def consult():
    # conexao
    conn = sqlite3.connect('post-it-database.db')
    conn.row_factory = sqlite3.Row
    curr = conn.cursor()
    # consulta
    curr.execute("SELECT nome, mensagem, datetime(criado_em,'localtime') as criado_em FROM post ORDER BY criado_em DESC")
    rows = curr.fetchall()
    return rows

def save(nome, mensagem):
    # conexao
    conn = sqlite3.connect('post-it-database.db')
    curr = conn.cursor()  
    #salva
    curr.execute("INSERT into post (nome, mensagem) values (?,?)",(nome,mensagem))  
    conn.commit()  

@app.route("/")
def home():
    try:
        rows = consult()
        print("Efetuando consulta no SQLite.") 
        return render_template('index.html', posts = rows, show_modal=False )
    except Exception as e:
        print(e)

@app.route("/salvar", methods = ["POST","GET"])
def salvar():
     if request.method == "POST":
        try:
            name = request.form["nome"]  
            message = request.form["mensagem"]  
            save(name, message)                     
            rows = consult()
            print("Salvando dados no SQLite.")   
            return render_template('index.html', posts = rows, show_modal=True)         
        except Exception as e: 
            print(e)

if __name__ == '__main__':
    app.run(debug = True)