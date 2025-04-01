from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_word():
    data = request.get_json()
    word = data.get('word')

    # Dummy logic for classification
    if word.lower() in ['cat', 'dog', 'animal']:
        result = 'Animal'
        image_url = url_for('static', filename='images/pexels-svetozar-milashevich-99573-1490908.jpg')
    elif word.lower() in ['doctor', 'physician', 'person']:
        result = 'Person'
        image_url = url_for('static', filename='images/male-doctor-smiling-happy-face-600nw-2481032615.webp')
    else:
        result = 'Object'
        image_url = url_for('static', filename='images/NationalGeographic_1468962.avif')

    return jsonify({'result': result, 'image_url': image_url})

if __name__ == '__main__':
    app.run(debug=True)
