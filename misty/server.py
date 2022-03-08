import os
import urllib.request
import base64
from flask import Flask, request, redirect, jsonify, send_from_directory, abort
from flask_restful import Api, Resource, reqparse
from werkzeug.utils import secure_filename


app = Flask(__name__)
api = Api(app)
app.secret_key = ''
app.config['UPLOAD_FOLDER'] = ''
app.config['MAX_CONTENT_LENGTH'] = 128 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_DIRECTORY = "data/audio_files"
count = 0


@app.route("/files")
def list_files():
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)


@app.route("/files/<path:path>")
def get_file(path):
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


@app.route("/files/<filename>", methods=["POST"])
def post_file(filename):

    if "/" in filename:
        abort(400, "no subdirectories allowed")
    split = filename.split('.')
    new_filename = 'new_{}{}.{}'.format(split[0], count, split[1])
    while os.path.exists(os.path.join(UPLOAD_DIRECTORY, new_filename)):
        count += 1
        new_filename = 'new_{}{}.{}'.format(split[0], count, split[1])
    with open(os.path.join(UPLOAD_DIRECTORY, new_filename), "wb") as fp:
        decode_string = base64.b64decode(request.data)
        fp.write(decode_string)

    # Call to privacy controller and text to speech

    
    
    return 'http://35.3.86.69:5000/files/{}'.format(filename), 201


if __name__ == "__main__":
    api.run(debug=False, port=8000)
