
from flask import *
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run()

@app.route("/", methods =["GET" , "POST"])
def home():
    if request.method == "POST" :
        print(request.form["name"])
        print(request.form["surname"])
        print(request.form["email"])
        return
    
    return render_template("home.html")


