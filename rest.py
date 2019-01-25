from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/<int:num>*<int:mult>', methods=['GET'])
def multiply(num, mult):
    return jsonify({'result': num*mult})
@app.route('/<int:num>/<int:div>', methods=['GET'])
def divide(num, div):
    return jsonify({'result': num/div})
@app.route('/<int:num>+<int:adder>')
def add(num, adder):
    return jsonify({'result': num+adder})
@app.route('/<int:num>-<int:subtractor>')
def subtract(num, subtractor):
    return jsonify({'result': num-subtractor})

if __name__ == "__main__":
    app.run(port=8000, debug=True)