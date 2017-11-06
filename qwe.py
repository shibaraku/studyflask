from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.qq.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME='30904978',
    MAIL_PASSWORD='fxowepskukchbjhe'
)

mail = Mail(app)


@app.route('/')
def index():
    msg = Message(subject="lalala", sender='30904978@qq.com', recipients=['30904978@qq.com'])
    msg.html = '<h1>hello world！</h1>'
    mail.send(msg)
    return "hello_world"


if __name__ == '__main__':
    app.run()
