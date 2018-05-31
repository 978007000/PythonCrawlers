import redis
import json

r = redis.Redis(host='34.229.250.31',port=6379,db=3)

keys = r.keys()

for key in keys:
    res = r.get(key)
    res = json.loads(res.decode('utf-8'))
    print (res.get('result'))