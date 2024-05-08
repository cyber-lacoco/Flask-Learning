from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
#working with Jinja2 Engine
#mera 
name = "Satar"
@app.route('/')
def home():
    return render_template('index.html', Name=name)

@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)