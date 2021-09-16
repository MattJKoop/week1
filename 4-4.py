from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
 return '<h1>Hello World!</h1>'
@app.route('/user/<name>')
def user(name):
 return '<h1>Hello, %s!</h1>' % name
if __name__ == '__main__':
 app.run(debug=True)
@app.route('/', methods=['GET', 'POST'])
def index():
 name = None
 form = NameForm()
 if form.validate_on_submit():
    name = form.name.data
    form.name.data = ''
 return render_template('index.html', form=form, name=name)