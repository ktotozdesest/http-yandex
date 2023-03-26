from flask import Flask, url_for, render_template, redirect
from form import Form

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sec-key'


@app.route('/<title>')
@app.route('/index/<title>')
def base(title):
    return render_template('base.html', title=f'{title}')
   

@app.route('/training/<prof>')
def training(prof):
    param = {}
    param['prof'] = prof
    param['title'] = prof
    return render_template('training.html', **param)


@app.route('/list_prof/<list>')
def list_prof(list):
    param = {}
    param['title'] = list
    param['list'] = list
    param['profs'] = ['Врач', 'Другой врач', 'Третий врач', 'Тех... а нет врач', 'Тоже врач']
    return render_template('list.html', **param)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    param = {}
    param['title'] = 'title'
    param['answer'] = ['Фамилия: ௵؎൹༚౿௶؎൹୰', 'Имя: ௴௵؎൹௶؎௵௺', 'Образование: строитель звезды смерти',
                       'Пол: Владыка мира', 'Мотивация: Вернуться на родину', 'Остаться на марсе: True']
    return render_template('auto_answer.html', **param)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Form()
    param = {}
    param['title'] = 'title'
    param['form'] = form
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('form.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
