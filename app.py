import os
from flask import Flask, jsonify, request

app = Flask(__name__)

currid = { 'currid': 1 }

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/todo/api/v1.0/currid', methods=['GET'])
def get_id():
	return jsonify(currid)

# @app.route('/todo/api/v1.0/currid/<int:newid>', methods = ['PUT'])
# def update_id():
# 	currid = { 'currid:' newid }
# 	return currid

@app.route('/todo/api/v1.0/currid/', methods = ['POST'])
def post_id():
	currid = { 'currid': request.json['newid'] }
	return currid
	# return jsonify({'currid': currid}), 201

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)