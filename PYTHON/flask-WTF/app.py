from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'teddylikeabear'

class MyForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        # Process form data here
        name = form.name.data
        # Do something with the data
    return render_template('index.html', form=form)
