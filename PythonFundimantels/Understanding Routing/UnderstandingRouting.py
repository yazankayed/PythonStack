from flask import Flask  
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'
@app.route('/dojo')          
def dojo():
    return "Dojo"
@app.route('/flask')
def flask():
    return "Hi Flask!"
@app.route('/micheal')
def micheal():
    return "Hi Micheal!"
@app.route('/jhon')
def jhon():
    return "Hi Jhon!"

@app.route('/repeat/<xx>/<word>')
def repeat(xx, word):
    ans = ""
    for i in range(int(xx)):
        ans += word
    return ans

if __name__=="__main__":        
    app.run(debug=True)     
