from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Λίστα για προσωρινή αποθήκευση URLs εικόνων
pictures = []

@app.route('/pictures', methods=['GET'])
def get_pictures():
    return jsonify(pictures), 200

@app.route('/pictures', methods=['POST'])
def add_picture():
    if not request.json or 'url' not in request.json:
        abort(400)
    url = request.json['url']
    picture = {'url': url}
    pictures.append(picture)
    return jsonify(picture), 201

@app.route('/pictures', methods=['DELETE'])
def delete_pictures():
    pictures.clear()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
