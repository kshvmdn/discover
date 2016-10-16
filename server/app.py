#!/usr/bin/env python
import os
from flask import abort, Flask, jsonify, request
from flask_cors import CORS, cross_origin

from fetch import fetch

VERSION = '1.0'

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
CORS(app)


@app.route('/api/%s/<string:owner>/<string:repo>' % VERSION)
def api(owner, repo):
    data = fetch(owner, repo)
    return jsonify(meta=dict(status=200, message='OK'),
                   data=sorted(data, key=lambda r: r['count'], reverse=True))


@app.errorhandler(400)
@app.errorhandler(403)
@app.errorhandler(404)
def bad_request(error):
    response = jsonify(meta=dict(status=error.code, message=error.description))
    return response, error.code

if __name__ == '__main__':
    HOST, PORT, DEBUG = os.environ.get('HOST', '0.0.0.0'), \
        os.environ.get('PORT', 3001), os.environ.get('DEBUG', False)

    app.run(host=HOST, port=int(PORT), debug=DEBUG)
