from flask import Flask, render_template

app = Flask(__name__, template_folder='./template', static_folder='./static')


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
        'инженер-исследователь', 'пилот', 'строитель', 'экзобиолог',
        'врач', 'инженер по терраформированию', 'климатолог',
        'специалист по радиационной защите', 'астрогеолог',
        'гляциолог', 'инженер жизнеобеспечения', 'метеоролог',
        'оператор марсохода', 'киберинженер',
        'штурман', 'пилот дронов']
    return render_template('prof.html', list=list, prof=prof)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    a = {'title': 'Анкета', 'surname': 'Watny', 'name': 'Mark', 'education': 'выше среднего',
         'profession': 'штурман марсохода', 'sex': 'male',
         'motivation': 'Всегда мечтал застрять на Марсе!', 'ready': 'True'}
    return render_template('auto_answer.html', answer=a)


@app.route('/login')
def login():
    return render_template('autorization.html', title='Аварийный доступ')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
