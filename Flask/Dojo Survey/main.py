from flask import Flask, render_template, request
app = Flask(__name__)                     

@app.route('/')                           
def show_template():
    return render_template('index.html')  
    
@app.route("/result", methods=["POST"])
def proccess_info():
    return render_template("info.html" , name= request.form["username"] , lc = request.form ["locations"] , 
                        lang = request.form["langs"] , com_op = request.form["Comment"])

if __name__=="__main__":
    app.run(debug=True)        
