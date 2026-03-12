from flask import Flask, render_template,request
import requests
import smtplib
from email.mime.text import MIMEText
user_email = "pushpendra22200504@gmail.com"
user_password = "wnfn txyv nows pukh"
reciever_email = "pushpendra2242005@gmail.com"
API_KEY = "https://api.npoint.io/cf96eab96e4b77125724"
data = requests.get(API_KEY)
data_json = data.json()
app = Flask(__name__)
@app.route("/")
def home_fun():
    return render_template("index.html",file_location="static/assets/img/home-bg.jpg",blogs_data=data_json)
@app.route("/about")
def about_fun():
    return render_template("about.html",file_location="static/assets/img/about-bg.jpg")
@app.route("/contact")
def contact_fun():
    return render_template("contact.html",file_location="static/assets/img/contact-bg.jpg")
@app.route("/post/<int:post_id>")
def post_fun(post_id):

    for content in data_json:
        if content["id"] == post_id:
            #Problem there fix when we click any post redirect
            # to individual blog post page using url_for
            # file_des = content["image_url"]
            # title = content["title"]
            return render_template("post.html",post_content=content)
    return "error"
@app.route("/form_entry",methods=["POST"])
def recieve_date():
    name = request.form["name"]
    email = request.form["email"]
    phone_no = request.form["phone"]
    message = request.form["message"]
    send_message= (f"User message and detail\n"
            f"{name}\n"
            f"{email}\n"
            f"{phone_no}\n"
            f"{message}\n")
    msg = MIMEText(send_message,"html")
    msg["Subject"] = "Clear blog post message"
    msg["From"] = user_email
    msg["To"] = reciever_email

    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls() #for secure message transfer
        server.login(user=user_email,password=user_password)
        server.send_message(msg)
        server.close()

    return "<h1>Successfully message send!</h1>"

if __name__ == "__main__":
    app.run(debug=True)