#!/usr/bin/env python3

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

ip_dict = {}

@app.route('/ip', methods=['GET', 'POST'])
def ip():
    try:
        mjson = request.get_json()
        if request.method == 'POST':
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ip = mjson['ip']
            name = mjson['name']
            ip_dict[name] = {'ip': ip, 'updateAT': ts}
            return 'OK'
        else:
            return jsonify(ip_dict)
    except Exception:
        return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0')

