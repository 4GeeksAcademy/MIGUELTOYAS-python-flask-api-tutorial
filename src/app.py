from flask import Flask, jsonify
from flask import request



app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]



@app.route('/todos', methods=['GET'])
def get_todos():
    # Devuelve la respuesta JSON directamente
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    # Add the new task to the todos list
    todos.append(request_body)
    # Return the updated list
    return jsonify(todos)










# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)