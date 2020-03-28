from flask import Flask, render_template, request
import os
import json
from random import randint

app = Flask(__name__, template_folder='./template', static_folder='./static')
index = 4


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


@app.route('/distribution')
def distribution():
    return render_template('distribution.html', people=['Ридли Скот', 'Энди Уир',
                                                        'Марк Уотни', 'Венката Капур',
                                                        'Тедди Сандерс', 'Шон Бин'])


@app.route('/table/<sex>/<int:age>')
def param(sex, age):
    return render_template('param.html', sex=sex, age=age)


@app.route('/galery', methods=['POST', 'GET'])
def galery():
    global index
    files = []
    for i in os.listdir('C:\\Users\\shelk\\.PyCharm2019.1\\config\\scratches\\flask-wtf\\static\\img'):
        if i.startswith('c') and i.endswith('.jpg'):
            files.append(i)
    print(files, request.method)
    if request.method == 'GET':
        return render_template('galery.html', files=files)
    elif request.method == 'POST':
        f = request.files['file']
        with open(f'static/img/c{index}.jpg', 'wb') as file:
            file.write(f.read())
        files.append(f'c{index}.jpg')
        index += 1
        return render_template('galery.html', files=files)


@app.route('/member')
def member():
    with open('./template/package.json', encoding='utf-8') as file:
        data = json.load(file)
    crew = data['crew']
    return render_template('member.html', a=crew[randint(0, len(crew) - 1)])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
# http://127.0.0.1:8080/member
