from flask import Blueprint, request,render_template,redirect,url_for
from app import mail,app
# from .models import ManageMail
from datetime import datetime
from flask_mail import Message


mail_blueprint=Blueprint("mail",__name__)

@mail_blueprint.route("/successfully-send-mail",methods=['GET',"POST"])
def Client_New_Mail(): 
    if request.method == "POST":  
        with app.app_context():             
            date=datetime.now().date()
            time=datetime.now().time()
            time_obj = datetime.strptime(str(time), "%H:%M:%S.%f")
            am_pm_time = time_obj.strftime("%I:%M:%S %p")
            data_new=send_email_to_client(
                                    request.form['name'],
                                    request.form['email'],
                                    request.form['subject'],
                                    request.form['phone'],
                                    request.form['country'],
                                    request.form['state'],
                                    request.form['city'],
                                    request.form['social_link'],
                                    request.form['message'],
                                    date=date,
                                    time=am_pm_time
                                )
            
            context={"email":request.form['email']}
            return render_template("my_protfolio/thankyou.html",**context)
    else:
       return redirect(url_for("welcome.PortfolioView"))

def send_email_to_client(name, email,subject, phone,country,state,city, social_link,result,date,time):
    with app.app_context():  
        msg = Message(subject="Your Mention Information",
                    sender="manavparmar283@gmail.com",
                    recipients=[email])
        context={
            "name":name,   
            "email":email,
            "subject":subject,
            "phone":phone,
            "country":country,
            "state":state,
            "city":city,
            "social_link":social_link,
            "result":result,
            "date":date,
            "time":time

        }

        msg.html = render_template("client_templates/client_mail.html",**context)

        mail.send(msg)
        data=send_email_to_admin(name, email,subject, phone,country,state,city, social_link,result,date,time)
        return data

def send_email_to_admin(name, email,subject, phone,country,state,city, social_link,result,date,time):
    with app.app_context():  
        msg = Message(subject="Client Message",
                    sender="manavparmar283@gmail.com",
                    recipients=["manavparmar283@gmail.com"])
        context={
            "name":name,
            "email":email,
            "subject":subject,
            "phone":phone,
            "country":country,
            "state":state,
            "city":city,
            "social_link":social_link,
            "result":result,
            "date":date,
            "time":time
        }

        msg.html = render_template("admin_templates/admin_mail.html",**context)

        mail.send(msg)
        return "Done"