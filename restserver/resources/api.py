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
    cmd = "peer channel create -o orderer.example.com:7050 -c businesschannel -f ./channel-artifacts/channel.tx"
    status, out = commands.getstatusoutput(cmd=cmd)
    if status != 0:
        return make_fail_resp(error="peer channel create failed",
                              data={"msg": out})
    return make_ok_resp(data={"msg": out})


@ops_rest.route('/join_channel', methods=['GET'])
def join_channel():
    cmd = "peer channel join -b businesschannel.block -o orderer.example.com:7050"
    status, out = commands.getstatusoutput(cmd=cmd)
    if status != 0:
        return make_fail_resp(error="peer channel join failed",
                              data={"msg": out})
    return make_ok_resp(data={"msg": out})


@ops_rest.route('/update_anchor_peers', methods=['GET'])
def update_anchor_peers():
    cmd = "peer channel create -o orderer.example.com:7050 -c businesschannel -f ./channel-artifacts/Org1MSPanchors.tx"
    status, out = commands.getstatusoutput(cmd=cmd)
    if status != 0:
        return make_fail_resp(error="peer channel create failed",
                              data={"msg": out})
    return make_ok_resp(data={"msg": out})
