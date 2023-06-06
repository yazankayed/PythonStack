from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def counter():
    
    session['Counter']=session['Counter']+1
    return render_template("index.html",Counter=session['Counter'])


@app.route('/destroy',methods=["post"])
def destroy():
    session.clear
    session['Counter']=0
    return redirect("/") 

if __name__=="__main__":
    app.run(debug=True)   