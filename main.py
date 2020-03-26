from flask import Flask, render_template

app = Flask(__name__, template_folder='./template')


@app.route('/<string:title>')
@app.route('/index/<string:title>')
def render(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('base.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
