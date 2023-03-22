from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/definition/<word>')
def get_definition(word):
    with open('dictionary.txt') as f:
        for line in f:
            if line.startswith(word + ' '):
                definition = line.strip().split(' ', 1)[1]
                return jsonify({word: definition})
    return jsonify({word: 'not found'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
