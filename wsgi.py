#from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy

#import connexion

#app = connexion.App(__name__, specification_dir='./')

#app.add_api('swagger.yml')

#@app.route('/')
#def home():
    #return render_template('home.html')
from app import create_app
import os

app = create_app()
app.app_context().push()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=int(os.environ.get("PORT", 5000)))