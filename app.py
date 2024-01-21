from flask import Flask
from todos import todo
from authentication import auth

app = Flask(__name__)

app.register_blueprint(todo)
app.register_blueprint(auth)

if __name__=='__main__':
    app.run(debug=True)
