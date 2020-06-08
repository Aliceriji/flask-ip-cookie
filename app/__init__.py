from flask import Flask,request
from static.pro1 import *
import random
from static.REDIS import REDIS

redis = REDIS()

app = Flask(__name__)

chooice_num = 0

@app.route('/')
def index():
    return '你的访问有误'

@app.route('/get/')
def get():
    pwd = request.args.get('pwd')
    lis = list(T_table.find({}))
    if pwd == passwrod:
        if len(lis) == 0:
            return '不存在ip'
        else:
            ip = random.choice(lis)
            return ip.get('pro').lower()+','+ip.get('str')
    elif pwd == 'height':
        return '当前存在ip数量:%s'%len(lis)
    elif pwd == 'log':
        title = ""
        with open(log_file,'r') as f:
            for i in f.readlines():
                title += '<p>%s</p>'%i.strip()
        return title
    else:
        return "你的访问有误"

@app.route('/get_chooice/')
def get_chooice():
    global chooice_num
    if chooice_num - 1 > len(redis):chooice_num = 1
    chooice = redis.keys()[chooice_num]
    chooice_num += 1
    pwd = request.args.get('pwd')
    if pwd == passwrod:
        return str(chooice)
    else:
        return "你的访问有误"

@app.route('/ip/get')
def ip_get():
    '返回请求的ip'
    return str(request.remote_addr)
