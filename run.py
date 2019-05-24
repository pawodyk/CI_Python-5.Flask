import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "very_secret_key"

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)
    
@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    
    return render_template("member.html", member=member)
    
@app.route("/contact", methods=["GET", "POST"])
def contact(): 
    if request.method == "POST":
        print(request.form)
        flash("Thanks {}, we have recived your massage!".format(request.form[name]))
        
    return render_template("contact.html", page_title="Contact")
    
@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    
    #configuration used to host the website in the cloud9
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")), 
            debug=True)
            
    #configuration used to host on the local server
    #app.run(host="127.0.0.1", port="5500", debug=True)
            
            
    