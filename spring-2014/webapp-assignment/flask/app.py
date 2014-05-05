# all the imports
import os
import sqlite3
import json
from flask import Flask, g, render_template, make_response

app = Flask(__name__)
app.config.from_object(__name__)

########## SETTINGS (CHANGE THESE TO FIT YOUR APP) ##########

DATABASE = 'campfin.sqlite'
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

########## APP CODE (CHANGE THIS ) ##########

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/data")
def crime_static():
    template = render_template("crime_data.json")
    response = make_response(template)
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route("/data-dynamic")
def crime_dynamic():
    # Access and query our database
    connection = get_db()
    cursor = connection.execute('select * from contributions;')

    # Turn the query results into dictionaries
    dispatches = []
    for row in cursor.fetchall():
        dispatches.append(dict(row))

    # Turn the data into JSON
    template = json.dumps(dispatches)

    # Return JSON to the browser
    response = make_response(template)
    response.headers['Content-Type'] = 'application/json'
    return response

########## EXECUTION BOILERPLATE (ALSO DON'T CHANGE THIS) ##########

if __name__ == "__main__":
    app.run(debug=True)
