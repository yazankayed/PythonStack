from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def playy():
    return ""
@app.route('/play/<x>')
def play(x):
    num_boxes = int(x)
    return render_template('play.html', num_boxes=num_boxes)

if __name__ == '__main__':
    app.run()
