from static.pro1 import *
import threading
import requests
import time

sem = threading.Semaphore(thread_num)
lock = threading.Lock()

def add_ip(ip):
    with sem:
        proxies = {
            ip['pro'].lower():ip['str']
        }
        try:
            resp = requests.get(url,proxies=proxies,timeout=timeout)
        except Exception as err:
            return None
        if resp.status_code == 200:
            if ip['ip'] in resp.text:
                lock.acquire()
                global_lis.append(ip)
                lock.release()
        else:
            return None

def run():
    while 1:
        lis = []
        ips = [i for i in list(table.find({})) if i.get('pro') and i.get('str')]
        for ip in ips:
            t = threading.Thread(target=add_ip,args=(ip,))
            lis.append(t)
            t.start()
        for t in lis:
            t.join()
        __lis = []
        for i in global_lis:
            del i['_id']
            __lis.append(i)
        T_table.delete_many({})
        T_table.insert_many(__lis)
        with open(log_file,'a') as f:
            f.write(time.strftime('%Y-%m-%d|%H:%M:%S')+':所有字线程结束一次\n')
        time.sleep(time_sleep)