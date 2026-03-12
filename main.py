from flask import Flask, render_template
import requests
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
if __name__ == "__main__":
    app.run(debug=True)