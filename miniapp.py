import logging
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

log = logging.getLogger(__name__)
try:
    import gpiozero
except:
    gpiozero = None

button = gpiozero.Button(2) if gpiozero is not None else None
red_led = gpiozero.LED(17) if gpiozero is not None else None

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    log.error(form.errors)
    if request.method == 'POST':
        name=request.form['name']
        log.info("Got new name: {}".format(name))

        if form.validate():
            # Save the comment here.
            if gpiozero is None:
                flash('Hello ' + name)
            else:
                flash("Hello {}, the button is {}".format(name,
                    "pressed" if button.is_pressed else "released"))
        else:
            flash('All the form fields are required. ')

    return render_template('hello.html', form=form)

if __name__ == "__main__":
    app.run()
