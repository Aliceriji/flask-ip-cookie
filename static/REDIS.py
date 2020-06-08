import redis
from static.pro import *
import pickle

class REDIS:

    def __init__(self,host=redis_hosts,port=redis_port,password=redis_pwd,db=0):
        self.redis = redis.StrictRedis(host=host,port=port,password=password,decode_responses=True,db=db)

    def All_get(self):
        dic = {}
        for key in self.redis.keys():
            dic[key] = self.redis.get(key)
        return dic

    def __len__(self):
        return len(self.redis.keys())

    def keys(self):
        return self.redis.keys()

    def del_All(self):
        for key in self.redis.keys():
            self.redis.delete(key)
        return '删除当前数据所有key'

    def __call__(self, *args, **kwargs):
        if len(args) > 2 or len(args) < 2:return '参数错误'
        self.redis.set(args[0],args[1])

    def save_bak(self):
        lis = [REDIS(db=i).All_get() for i in range(0,16)]
        with open(bak_file,'wb') as f:
            f.write(pickle.dumps(lis))
        return '保存成功'
