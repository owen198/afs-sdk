#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

STATUS_CODE = "statuscode"
ALLOWED_EXTENSIONS = ['pkl', 'bat']



@app.route('/pack', methods['GET'])
def upload():
    try:
        subprocess.call(["/afs-sdk/ota/otapackager-cli", 
                                 "-i", "/afs-sdk/ota/model/", 
                                 "-d", "/afs-sdk/", 
                                 "-b", "model.pkl"])
        return jsonify({STATUS_CODE:200}), 200
    except:
        return jsonify({STATUS_CODE:500}), 500




@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']
        file_path = request.form['file_path']  
        if file and allowed_file(file.filename):
	    filename = os.path.join(file_path, file.filename)
            file.save(filename)

            return jsonify({STATUS_CODE:200}), 200
    except ValueError:
        return jsonify({STATUS_CODE:211}), 400
    except IOError:
        return jsonify({STATUS_CODE:212}), 400
    except :
	return jsonify({STATUS_CODE:500}), 500

def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
