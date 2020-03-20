# -*- encoding: utf-8 -*-
from pymongo import MongoClient
#  RROH1QMDW1vzXs9T
#uri = "mongodb://inegi:rsF7vS5QFZmUCLTHNo7sEYTN3lOxVkHJSH6Vf3xlSGbj8hXzM3hGxZHNxTe9Fny296ya4BgjnSetDZyrj4b8yA==@inegi.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
uri = "mongodb://Edgar:JMifLfai75Leg16n@cluster-shard-00-00-xf0s3.gcp.mongodb.net:27017/base?ssl=true&replicaSet=Cluster-shard-0&authSource=admin&retryWrites=true&w=majority"
client = MongoClient(uri)
mongo = client['base']
client.close()