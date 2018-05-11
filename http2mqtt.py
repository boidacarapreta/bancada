from paho.mqtt import publish
import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def default():
    return "It works!"

@app.route('/a/<operacao>', methods=['POST'])
def a(operacao):
    publish.single('a', operacao, hostname='nuvem.sj.ifsc.edu.br')
    return operacao

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
