from flask import Flask, render_template

app = Flask(__name__, template_folder='./template')


@app.route('/<string:title>')
@app.route('/index/<string:title>')
def render(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('base.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    prof = [
        'инженер-исследователь',
        'пилот', 'строитель', 'экзобиолог',
        'врач', 'инженер по терраформированию', 'климатолог',
        'специалист по радиационной защите', 'астрогеолог',
        'гляциолог', 'инженер жизнеобеспечения', 'метеоролог',
        'оператор марсохода', 'киберинженер',
        'штурман', 'пилот дронов']
    return render_template('prof.html', list=list, prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
