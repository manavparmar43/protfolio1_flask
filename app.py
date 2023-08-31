from flask import Flask
import os
from dotenv import load_dotenv
from flask_mail import Mail

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv('SECRETE_KEY')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'manavparmar283@gmail.com'
app.config['MAIL_PASSWORD'] = 'pammnsscfmkhcxjs'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True



mail = Mail(app)
from ManageMail.views import mail_blueprint
from portfolio.views import portfolio_blurprint
app.register_blueprint(mail_blueprint)
app.register_blueprint(portfolio_blurprint)
if __name__ == '__main__':
    app.run(debug=True)