from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def playy():
    return ""
@app.route('/play/<x>/<color>')
def play(x, color):
    num_boxes = int(x)
    return render_template('index.html', num_boxes=num_boxes, color=color)

if __name__ == '__main__':
    app.run()
 