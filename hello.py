from flask import Flask, render_template, flash, url_for
from flask_wtf import FlaskForm #Imported Flask Form
from wtforms import StringField, SubmitField #String field an Submit Field handles Input and Button actions of a form
from wtforms.validators import DataRequired #To validate Data
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime #Cntracting time they're added


#Creating a flask Instance
app = Flask(__name__) 
#Adding a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#Created a secret key to Implement CSRF[Created an Environment variable called SECRET_KEY and added to app.config]
app.config['SECRET_KEY'] = "My Super Secrete Key" #CSRF Validation Key
#Initialize The Database
db = SQLAlchemy(app)
app.app_context().push()

#Create a Model
class Users(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(200), nullable=False)
   email =  db.Column(db.String(100), nullable=False, unique=True)
   date_added = db.Column(db.DateTime, default=datetime.now()) 

   #Create string
   def __repr__(self):
      return '<Name &r>' % self.name

#Create a form class
class UserForm(FlaskForm): #Created a class Nameform to inherit FlaskForm
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")

#Create a form class
class NamerForm(FlaskForm): #Created a class Nameform to inherit FlaskForm
    name = StringField("What's your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/user/add/', methods=['GET', 'POST'])
def add_user():
   form = UserForm()
   name = None
   if form.validate_on_submit():
      user = Users.query.filter_by(email=form.email.data).first()
      if user is None:
         user = Users(name=form.name.data, email=form.email.data)
         db.session.add(user)
         db.session.commit() 
      name = form.name.data
      flash('User added Successfully')
   our_users = Users.query.order_by(Users.date_added)
   return render_template('add_user.html', 
                          form=form,
                          name=name,
                          our_users = our_users
                          )


#working with Jinja2 Engine
name = "Satar"
@app.route('/') #Created a route decorator
def home():
    name = 'Satar' 
    stuff = "this is a strong tag "
    flash("Welcome to The home page")
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
      flash("Form submitted successfully")
   return render_template('name.html',  form=form, name=name)

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