from flask import Flask
from config import CONFIG_DEBUG,CONFIG_PORT

app = Flask(__name__)

from routes import chat
from routes import index

app.register_blueprint(index.bp_teste)
app.register_blueprint(chat.bp_chat)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=CONFIG_PORT,debug=CONFIG_DEBUG)
