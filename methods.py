from base import mongo
from base import client
import json
from bson.json_util import dumps
from bson.son import SON
from bson.objectid import ObjectId
from flask import request
import socket
import re
import xlrd
import pandas as pd



def dump(query):
	json = dumps(query,indent=1, ensure_ascii=False).encode('utf8')
	return json

def loadFile(request):
    file = request.files['file']
    #filename = request['filename']
    event = request.form['filename']
    data_xls = pd.read_excel(file)
    json_array = data_xls.to_json(orient='records')
    data = json.loads(json_array)
    mongo.persons.drop()
    for inv in data:
        inv['EVENTO']=event
        mongo.persons.insert(inv)
    return "200", 201

def register(data):
    res = json.loads(data)
    mongo.users.insert(res)
    return "user added", 200

def findPerson(data):
    res = json.loads(data)
    #print(res)
    name = str(res['name'])
    pat = re.compile(r'{}'.format(name), re.I)
    keys = mongo.persons.find_one({})
    pipeline = []
    for key, value in keys.items():
        param = {key:{'$regex':pat}}
        pipeline.append(param)
    if name == '':
        resp = "404", 204
        return resp
    else:
        res = mongo.persons.find({'$or':pipeline},{'EVENTO':0})
        #res = mongo.persons.find({'$or':[{"GRADUADO":{'$regex': pat}},{"INVITADO":{'$regex': pat}}]})
        resp = dumps(res)
        if resp == "[]":
            return resp, 204
        return resp, 200

def users():
    res = mongo.users.find({})
    resp = dumps(res)
    #print(resp)
    if resp == "[]":
        return resp, 204
    return resp, 200

def getUser(data):
    res = json.loads(data)
    username = str(res['username'])
    password = str(res['password'])
    if(username == ''):
        resp = "404", 204
        return resp
    else:
        res = mongo.users.find({'username':username,'password':password})
        resp = dumps(res)
        #print(resp)
        if resp == "[]":
            return resp, 204
        return resp, 200