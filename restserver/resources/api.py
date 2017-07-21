import os
import sys
import commands

from flask import Blueprint

from common import make_ok_resp, make_fail_resp

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

ops_rest = Blueprint('ops_rest', __name__,
                     url_prefix='/{}'.format("api"))

@ops_rest.route('/create_channel', methods=['GET'])
def create_channel():
    return make_ok_resp(data={})