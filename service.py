from flask import Flask
from flask import request
import socket
import os
import sys
import requests


app = Flask(__name__)


@app.route('/service', methods=['GET', 'POST'])
def service():
	app.logger.info(request.json)
	return socket.gethostbyname(socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ['PORT']), debug=True)
