import os
import sys
import commands

from flask import Blueprint
from flask import request as r

from common import make_ok_resp, make_fail_resp

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

ops_rest = Blueprint('ops_rest', __name__,
                     url_prefix='/{}'.format("api"))


@ops_rest.route('/create_channel', methods=['GET'])
def create_channel():
    cmd = "peer channel create " \
          + "-o orderer.example.com:7050 -c businesschannel -f ./channel-artifacts/channel.tx"
    status, out = commands.getstatusoutput(cmd=cmd)
    if status != 0:
        return make_fail_resp(error="peer channel create failed",
                              data={"msg": out})
    return make_ok_resp(data={"msg": out})


@ops_rest.route('/join_channel', methods=['GET'])
def join_channel():
    cmd = "peer channel join " \
          + "-b businesschannel.block -o orderer.example.com:7050"
    status, out = commands.getstatusoutput(cmd=cmd)
    if status != 0:
        return make_fail_resp(error="peer channel join failed",
                              data={"msg": out})
    return make_ok_resp(data={"msg": out})


@ops_rest.route('/update_anchor_peers', methods=['GET'])
def update_anchor_peers():
    cmd = "peer channel create " \
          + "-o orderer.example.com:7050 -c businesschannel -f ./channel-artifacts/Org1MSPanchors.tx"
    status, out = commands.getstatusoutput(cmd=cmd)
    if status != 0:
        return make_fail_resp(error="peer channel create failed",
                              data={"msg": out})
    return make_ok_resp(data={"msg": out})


@ops_rest.route('/install_chaincode', methods=['POST'])
def install_chaincode():
    request_data = r.get_json(force=True, silent=True)
    if r.form:
        name = r.form["name"]
        version = r.form["version"]
        path = r.form["path"]
    else:
        name = request_data.get("name")
        version = request_data.get("version")
        path = request_data.get("path")

    if not name or not version or not path:
        error_msg = "not enough arguments"
        return make_fail_resp(error=error_msg, data=r.form)

    cmd = "peer chaincode install " \
          + "-n {0} -v {1} -p {2} -o orderer.example.com:7050".format(name, version, path)
    status, out = commands.getstatusoutput(cmd=cmd)
    if status != 0:
        return make_fail_resp(error="peer chaincode install failed",
                              data={"msg": out})
    return make_ok_resp(data={"msg": out})


@ops_rest.route('/instantiate_chaincode', methods=['POST'])
def instantiate_chaincode():
    request_data = r.get_json(force=True, silent=True)
    if r.form:
        name = r.form["name"]
        version = r.form["version"]
        ctor = r.form["ctor"]
    else:
        name = request_data.get("name")
        version = request_data.get("version")
        ctor = request_data.get("ctor")

    if not name or not version or not ctor:
        error_msg = "not enough arguments"
        return make_fail_resp(error=error_msg, data=r.form)

    cmd = "peer chaincode instantiate " \
          + "-o orderer.example.com:7050 -C businesschannel " \
          + "-n {0} -v {1} -c {2} -P \"OR ('Org1MSP.member')\"".format(name, version, ctor)
    status, out = commands.getstatusoutput(cmd=cmd)
    if status != 0:
        return make_fail_resp(error="peer chaincode instantiate failed",
                              data={"msg": out})
    return make_ok_resp(data={"msg": out})
