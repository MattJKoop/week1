from flask import Flask, render_template, session, redirect, url_for
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
 return '<h1>Hello World!</h1>'
if __name__ == '__main__':
 app.run(debug=True)
@app.route('/', methods=['GET', 'POST'])
def index():
 form = NameForm()
 if form.validate_on_submit():
    session['name'] = form.name.data
 return redirect(url_for('index'))
 return render_template('index.html', form=form, name=session.get('name'))
