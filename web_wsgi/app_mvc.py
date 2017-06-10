from flask import Flask,request,render_template


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/signin',methods=['GET'])
def singin():
    return render_template('signin.html')

@app.route('/signin',methods=['POST'])
def login():
    username=request.form['username']
    password=request.form['password']
    if username=='huu' and password=='hubang1994':
        return render_template('signin_ok.html',username=username)
    else:
        return render_template('signin.html',message='Sorry!!',username=username)
if __name__ == '__main__':
    app.run()