from flask import Flask

app=Flask(__name__)

@app.route("/")
def home_page():
    
    return "Hello user welcome to our program"

@app.route("/about")
def about():
    return "This programmer demo magazine"



@app.route("/contact")
def contact():
    return "Conatct email@mail.com"
    
if __name__=="__main__":
    app.run()