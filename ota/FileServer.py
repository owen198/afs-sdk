#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shlex
import shutil
from flask import Flask, jsonify, request, send_file
import subprocess

app = Flask(__name__)

STATUS_CODE = 'statuscode'
ALLOWED_EXTENSIONS = ['pkl', 'bat']

PATH_ROOT = os.path.dirname(os.path.abspath(__file__))
PATH_OTA = os.path.join(PATH_ROOT, 'ota')
PATH_MODEL = os.path.join(PATH_OTA, 'model')

if not os.path.isdir(PATH_MODEL):
    #os.makedirs(PATH_MODEL, exist_ok=True)
    os.makedirs(PATH_MODEL)

NAME_PACK = 'model.zip'
NAME_MODEL = 'model.pkl'
NAME_BATCH = 'model.bat'
CMD_OTA = os.path.join(PATH_ROOT, 'otapackager-cli')
ALLOWED_UPLOADED = [NAME_MODEL, NAME_BATCH]


@app.route('/pack', methods=['GET'])
def pack():
    try:
        # clean pervious package
        clean_pervious(PATH_MODEL, '.zip')
        clean_pervious(PATH_OTA, '.zip')
        clean_pervious(PATH_ROOT, '.zip')

    except Exception as e:
        print('error at clean_pervious, err_msg: {0}'.format(e))
        return jsonify({STATUS_CODE: 500}), 500

    try:
        # chech if bat and pkl file exist or not
        if not os.path.isfile(os.path.join(PATH_MODEL, NAME_BATCH)):
            return jsonify({STATUS_CODE: 211}), 200
        if not os.path.isfile(os.path.join(PATH_MODEL, NAME_MODEL)):
            return jsonify({STATUS_CODE: 212}), 200

        # pack both pkl and bat
        # cannot setup equal input(-i) and dest(-d), therefore setup -d as PATH_OTA
        # will need move output file
        cmd = CMD_OTA + ' -i ' + PATH_MODEL + ' -d ' + PATH_OTA + ' -b ' + NAME_BATCH
    except Exception as e:
        print('error before run cmd, err_msg: {0}, cmd: {1}'.format(e, cmd))
        return jsonify({STATUS_CODE: 500}), 500

    try:
        run_cmd = subprocess.Popen(shlex.split(cmd))
        print('{0} STDOUT: {1}'.format(CMD_OTA, run_cmd.stdout))
        print('{0} STDERR: {1}'.format(CMD_OTA, run_cmd.stderr))

    except Exception as e:
        print('error after run cmd, err_msg: {0}, cmd: {1}'.format(e, cmd))
        return jsonify({STATUS_CODE: 500}), 500

    try:
        # move file from PATH_OTA to PATH_MODEL
        for item in os.listdir(PATH_OTA):
            if item.endswith(".zip"):
                # remove ramdon number in file name
                src = os.path.join(PATH_OTA, item)
                dst = os.path.join(PATH_MODEL, item)
                shutil.move(src, dst)

        return jsonify({STATUS_CODE: 200}), 200

    except Exception as e:
        print(e)
        return jsonify({STATUS_CODE: 500}), 500


@app.route('/download', methods=['GET'])
def download():
    try:
        # get random file name
        filename = NAME_PACK
        for item in os.listdir(PATH_OTA):
            if item.endswith(".zip"):
                filename = item

        # if model.zip exists, return file to client
        if os.path.isfile(os.path.join(PATH_OTA, filename)):
            return send_file(
                os.path.join(PATH_OTA, filename), as_attachment=True)

        else:
            # file does not exists
            return jsonify({STATUS_CODE: 211}), 400

    except Exception as e:
        print(e)
        return jsonify({STATUS_CODE: 500}), 500

    finally:
        # delete file after download finished
        clean_pervious(PATH_OTA, ".zip")


@app.route('/upload', methods=['POST'])
def upload():
    try:
        file = request.files['file']
        file_path = PATH_MODEL

        # if file extension is allowable, clean pervious files and upload to PATH_MODEL
        if file and allowed_file(file.filename):

            #clean pervious files
            clean_pervious(PATH_MODEL, file.filename.rsplit('.', 1)[1])
            #clean_pervious(PATH_MODEL, '.bat')

            filename = os.path.join(file_path, file.filename)
            file.save(filename)

            return jsonify({STATUS_CODE: 200}), 200
        else:
            return jsonify({STATUS_CODE: 213}), 200

    except ValueError:
        return jsonify({STATUS_CODE: 211}), 400
    except IOError:
        return jsonify({STATUS_CODE: 212}), 400
    except Exception as e:
        print(e)


def allowed_file(filename):
    #return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
    return '.' in filename in ALLOWED_UPLOADED


def clean_pervious(dir_name=PATH_ROOT, extensions='.just_give_one'):
    for item in os.listdir(dir_name):
        if item.endswith(extensions):
            os.remove(os.path.join(dir_name, item))


if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=8088)
    app.run(debug=True, host='0.0.0.0', port=80)
