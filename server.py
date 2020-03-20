import os
import methods
from flask import jsonify, request, Flask
from flask_cors import CORS
from flask_restful import Api
from flask import make_response
from bson.json_util import dumps
import socket

ip = socket.gethostbyname(socket.gethostname())
print(ip)
app = Flask(__name__)

@app.route('/')
def hello():
	return "Hola mundo!"

@app.route('/upload',methods=["POST"])
def code(): 
	resp = methods.loadFile(request)
	return resp

@app.route('/findPerson',methods=["POST"])
def findPerson(): 
    resp = methods.findPerson(request.data)
    return resp

@app.route('/getUser',methods=["POST"])
def getUser(): 
    resp = methods.getUser(request.data)
    return resp

@app.route('/users',methods=["GET"])
def users(): 
    resp = methods.users()
    return resp

@app.route('/register',methods=["POST"])
def register(): 
    resp = methods.register(request.data)
    return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api = Api(app)
api.representations = DEFAULT_REPRESENTATIONS

CORS(app)
if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 5000))
    app.run( port=5000,host=ip)#
    #app.run()