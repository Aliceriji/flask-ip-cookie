import pymongo

hosts = 'mongodb://pass@127.0.0.1:8001/'
# 修改数据库链接

log_file = '/var/log/users/app.log'
# 指定日志文件

T_table = pymongo.MongoClient(hosts)['ips']['TRUE_1']
# 指定测试完毕后，添加至的数据库

table = pymongo.MongoClient(hosts)['ips']['TRUE_1']
# 每一次都会循环去检测的总数据库

url = 'http://httpbin.org/ip'
# 检测的网址

timeout = 3
# 设置访问超时时间

port = 8008
# 配置网址访问端口，首先请添加防火墙规则
# firewall-cmd --permanent --add-port=80/tcp
# firewall-cmd --reload

passwrod = 'Alice'
# 访问时添加的pwd参数密码

thread_num = 10
# 指定的线程数量

global_lis = []
# 共有属性列表，进行储存ip

time_sleep = 3600
# 每次检测完后等待时间
