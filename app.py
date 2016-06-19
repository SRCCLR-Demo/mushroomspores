import os
from flask import Flask

app = Flask(__name__)

curr_id = [{ 'curr_id': 1 }]
@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_id():
	return jsonify({'curr_id': curr_id})

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)