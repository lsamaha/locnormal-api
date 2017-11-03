from flask import Flask, request
from postal.expand import expand_address
from postal.parser import parse_address
import json

app = Flask(__name__)


@app.route('/parse')
def parse():
    return json.dumps(do_parse(request.args.get('address', '')))


@app.route('/expand')
def expand():
    return str(do_expand(request.args.get('address', '')))


@app.route('/normal')
def normal():
    return str(do_expand(request.args.get('address', '')))


def do_parse(address):
    addr = {}
    addr_parts = parse_address(address)
    for v, k in addr_parts:
        addr[k] = v
    return addr


def do_expand(address):
    return expand_address(address)[0]


if __name__ == "__main__":
    app.run(debug=False, threaded=True, host='0.0.0.0')
