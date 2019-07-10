from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def make_boxes():
    print("the make boxes function is working")
    return render_template('index.html', times=2)

@app.route('/play/<num>')
def repeat_boxes(num):
    print(f"the boxes are repeating {num} times")
    return render_template('index.html', times=int(num))

@app.route('/play/<num>/<color>')
def make_color_change(num, color):
    print(f"the boxes are repeating {num} times and their color is {color}")
    return render_template('index.html', times=int(num), color=str(color))

if __name__=="__main__":
    app.run(debug=True)