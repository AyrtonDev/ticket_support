from flask import Flask, make_response, jsonify
from app.config.db import db_connection

app = Flask(__name__)

#jwt config

app.config['JWT_SECRET_KEY'] = 'ticket_support'

# BD config

cursor, conn = db_connection()

# routes
@app.route('/ping')
def ping():
    return make_response(jsonify({'pong': True}))

from app import routes
