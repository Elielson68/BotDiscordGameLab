from flask import Flask
from threading import Thread
import random


app = Flask(__name__)

@app.route('/')
def home():
	return 'Bot rodando!'

def create_app():
  app.run(
		host='0.0.0.0',
		port=random.randint(2000,9000)
	)

def keep_alive():
	'''
	Creates and starts new thread that runs the function run.
	'''
	t = Thread(target=create_app)
	t.start()