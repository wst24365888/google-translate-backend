import translatepy
from flask import Flask, request, jsonify

app = Flask(__name__)
translator = translatepy.Translator()


@app.route('/translate', methods=['POST'])
def translate():
    translationResult = translator.translate(request.json["source"], request.json["target-lang"])
    return jsonify({"source": request.json["source"], "result": translationResult.result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6666, debug=False)
