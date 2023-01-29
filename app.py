from flask import Flask, jsonify, request
from util import return_pred

app = Flask(__name__)


@app.post('/predict')
def predict():
    data = request.json
    try:
        sample = data['text']
    except KeyError:
        return jsonify({'error': 'No text sent'})

    sample = [sample]
    print(sample)
    predictions = return_pred(sample)
    try:
        result = jsonify(predictions[0])
    except TypeError as e:
        result = jsonify({'error': str(e)})
    return result

if __name__ == '__main__':
    app.run( debug=True, port = 1234)
