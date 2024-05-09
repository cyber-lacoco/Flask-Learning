from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm #Imported Flask Form
from wtforms import StringField, SubmitField #String field an Submit Field handles Input and Button actions of a form
from wtforms.validators import DataRequired #Tho validate Data


#Creating a flask Instance
app = Flask(__name__) 
#Created a secret key to Implement CSRF[Created an Environment variable called SECRET_KEY and added to app.config]
app.config['SECRET_KEY'] = "My Super Secrete Key" #CSRF Validation Key

#Create a form class
class NamerForm(FlaskForm): #Created a class Nameform to inherit FlaskForm
    name = StringField("What's your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


#working with Jinja2 Engine
name = "Satar"
@app.route('/') #Created a route decorator
def home():
    name = 'Satar'
    stuff = "this is a strong tag "
    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template('index.html', name=name, stuff=stuff, favorite_pizza=favorite_pizza)

# localhost:5050/user/name 
@app.route('/jinja')
def user():
   return render_template('base.html')

@app.route('/name', methods=['GET', 'POST'])
def user2():
   name = None
   form = NamerForm() #Called the class
   #Validate form 
   if form.validate_on_submit():
      name = form.name.data
      form.name.data = ''
   return render_template('name.html', name=name, form=form)

#Custom Error Pages
#Invalid Url
@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404
# INternal Server Error
@app.errorhandler(500)
def server_error(e):
 return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)