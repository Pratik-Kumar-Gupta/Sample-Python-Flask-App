from flask import Flask, jsonify, request
import logging


APP = Flask(__name__)

@APP.route('/testing/health', methods=['GET'])
def health():
    logging.info('Checking health')
    return jsonify({"Healthy": "true"})

if __name__ == '__main__':
    APP.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )