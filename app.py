from flask import Flask, render_template

app = Flask(__name__)


@app.route('/the/secret/garden')
def hello_world():
    return render_template('index.html')


@app.route('/clock')
def clock():
    return render_template('clock.html')


if __name__ == '__main__':
    app.run()
