from flask import Flask, request
from postal.expand import expand_address
from postal.parser import parse_address
from error import InvalidUsage
import json

app = Flask(__name__)
__max_addresses = 5000

@app.route('/parse')
def parse():
    return json.dumps(do_parse(request.args.get('address', '')))


@app.route('/expand')
def expand():
    return str(do_expand(request.args.get('address', '')))


@app.route('/normal')
def normal():
    params = request.args
    if 'address' in request.args:
        return str(do_expand(request.args.get('address', '')))
    elif 'addresses' in request.args:
        addresses_requested = json.loads(params.get('addresses'))
        num_addresses = len(addresses_requested)
        if num_addresses > __max_addresses:
            raise InvalidUsage(message="too many addresses (received %d max %d)" % (num_addresses, __max_addresses))
        addresses = list([do_expand(address) for address in addresses_requested])
        return str(json.dumps(addresses))


@app.errorhandler(InvalidUsage)
def handle_bad_request_param(e):
    return "Bad request %s" % e


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
