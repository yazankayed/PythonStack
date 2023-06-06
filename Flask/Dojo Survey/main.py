from flask import Flask, render_template, request
app = Flask(__name__)                     

@app.route('/')                           
def show_template():
    return render_template('index.html')  
    
@app.route("/result", methods=["POST"])
def proccess_info():
    
    data = {
        "name" : request.form["username"],
        "location" : request.form ["locations"],
        "lang" : request.form["langs"], 
        "comment" : request.form["Comment"],
    }

    return render_template("info.html" , data = data)

if __name__=="__main__":
    app.run(debug=True)        
