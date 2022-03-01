from flask import Flask, render_template

app = Flask(__name__)
#route -> where our site is going Flask_sit/something
#function -> What the site is going to show in the page
#template -> You have to have a directory called templates to flask identify what you want to render

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/users/<user_name>") #we use the user_name between <> cause we want to use it as a variable
def users(user_name):
    return render_template("users.html", user_name = user_name)

#starts the site
if __name__ == "__main__":
    app.run()