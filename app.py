from flask import Flask,render_template,jsonify,request,redirect
from flask_socketio import SocketIO, send

from model.User import User
from db import users

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)


#BLOQUE DE CONTROLADOR
    
@app.route("/")
def index():
    titulo = "EJEMPLOS:"
    lst = ['/user','/chat','/newChat']
    return render_template("index.html",titulo=titulo,lst=lst)



@app.route("/user",methods=['GET','POST','PUT','DELETE'])
def user_post():

    if request.method == 'GET':
        return render_template("user.html")
    elif request.method == 'POST':
        user = User()
        user.setUsername(request.form['username'])
        user.setPassword(request.form['password'])
        users.append(user.json())
        return jsonify(user)
        #return redirect("/")
    elif request.method == 'PUT':
        #return "entro put"
        jsonRequest = request.get_json()
        return jsonRequest['username']

@app.route('/prueba')
def prueba():
    return jsonify({'data':2})

@app.route('/chat')
def chat():
    return render_template("chat.html")

@app.route('/newChat')
def newChat():
    return render_template("newChat.html")

@socketio.on('message')
def handleMessage(msg):
    print("Message :" + msg['msg'])
    send(msg, broadcast = True)


#BLOQUE DE FINALIZADCION
if __name__ == "__main__":
    app.run(port=4000,debug=True,host="192.168.0.12")