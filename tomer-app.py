from flask import Flask, request
app = Flask(__name__)

@app.route('/whatismyname', methods=['GET', 'POST', 'DELETE'])
def hello():
    if request.method == 'GET':
        return '<font size=7>My name is Tomer</font>'
    elif request.method == 'POST':
        return 'creating your name'
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)

