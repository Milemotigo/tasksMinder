#!/usr/bin/python3
import os

# Set Flask app and debug mode
os.environ['FLASK_APP'] = 'app'
os.environ['FLASK_DEBUG'] = '1'

# Run the Flask app
os.system('flask run')

