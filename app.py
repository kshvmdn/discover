#!/usr/bin/env python

import os
from flask import abort, Flask, jsonify, render_template, request

from fetch import main as fetch

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:owner>/<string:repo>')
def results(owner, repo):
    depth = request.args.get('depth', 1, type=int)
    data = fetch(owner, repo, depth)

    return render_template('results.html', owner=owner, repo=repo, data=data)


@app.route('/api/<string:owner>/<string:repo>')
def api(owner, repo):
    depth = request.args.get('depth', 1, type=int)
    data = fetch(owner, repo, depth)

    return jsonify(meta=dict(status=200, message='OK'), data=data)


@app.errorhandler(400)
@app.errorhandler(403)
@app.errorhandler(404)
def bad_request(error):
    response = jsonify(meta=dict(status=error.code, message=error.description))
    return response, error.code

if __name__ == '__main__':
    HOST, PORT, DEBUG = (os.environ.get('HOST', '0.0.0.0'),
                         os.environ.get('PORT', 3000),
                         os.environ.get('DEBUG', False))

    app.run(host=HOST, port=int(PORT), debug=DEBUG)
