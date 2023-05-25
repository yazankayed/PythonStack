from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def playy():
    return ""
@app.route('/playyy')
def play():
    num_boxes = 8
    numm=(num_boxes*num_boxes)/2
    return render_template('index.html', n.umm)

if __name__ == '__main__':
    app.run()
