'''
Your assignment is to use the boilerplate app we've been building in class to produce JSON from
a new database, in this case of Medicare payments to doctors in Columbia. Specifically, you should
create a function that returns all of the data from the "doctors" table when someone visits the 
"/doctors" route in your application.

Most of the code below is boilerplate that you won't have to modify. You should only be changing
two areas: first, change the appropriate setting to connect the application to the "medicare.sqlite"
database (which is included in the repository). Second, write a function that produces the JSON.
'''

########## IMPORTS (DON'T CHANGE THESE) ##########

import os
import sqlite3
import json
from flask import Flask, g, render_template, make_response

app = Flask(__name__)
app.config.from_object(__name__)

########## SETTINGS (CHANGE THESE AS APPROPRIATE) ##########

DATABASE = ''
USERNAME = ''
PASSWORD = ''

########## DATABASE CONNECTION BOILERPLATE (DO NOT CHANGE THIS) ##########

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, DATABASE),
    DEBUG=True,
    SECRET_KEY='',
    USERNAME=USERNAME,
    PASSWORD=PASSWORD
))

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

########## APP CODE (YOUR FUNCTION GOES HERE) ##########







########## EXECUTION BOILERPLATE (ALSO DON'T CHANGE THIS) ##########

if __name__ == "__main__":
    app.run(debug=True)
