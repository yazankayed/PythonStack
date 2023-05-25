from flask import Flask, render_template,request
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html ")


@app.route('/result')
def result():
    user_name=request.form['username']
    user_location=request.form['locations']
    user_lang=request.form['langs']
    user_comment=request.form['Comment']
    return render_template("result.html ",user_name= )



if __name__ == "__main__":
    app.run(debug=True)

