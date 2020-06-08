from driver import LINUX_DRIVER as Driver
from pyquery import PyQuery as pq
import threading
import time
import requests
from static.REDIS import *
from static.pro import *

sem = threading.Semaphore(thread_num)
lock = threading.Lock()

class LOGIN:

    def __init__(self):
        self.main()
        self.redis = REDIS()

    def ret_headers(self,cookie):
        return {
            'User-Agent':"Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
            'cookie':cookie
        }

    def main(self):
        self.users = {}
        with open('../static/user+pwd.txt', 'r') as f:
            lis = f.read().strip().split('\n')
        for i in lis:
            user,pwd = i.split(':')
            self.users[user] = pwd
        return True

    def ret_cookice(self,cookies):
        dic = {}
        for cookie in cookies:
            dic[cookie['name']] = cookie['value']
        title = ''
        for i in dic:
            title += i + '=' + dic[i] + ';'
        return dic,title

    def login(self,user,pwd):
        def inner():
            with sem:
                D = Driver()
                driver = D.Ret_driver()
                driver.get('https://www.instagram.com')
                time.sleep(3)
                inp = driver.find_elements_by_class_name('_2hvTZ')
                inp1 = inp[0]
                inp2 = inp[-1]
                inp1.send_keys(user)
                time.sleep(1.5)
                inp2.send_keys(pwd)
                time.sleep(1.5)
                but1 = driver.find_elements_by_class_name('sqdOP')[1]
                but1.click()
                time.sleep(10)
                dic,title = self.ret_cookice(driver.get_cookies())
                D.del_driver()
                lock.acquire()
                print('账号:%s完成'%user)
                self.redis(user,title)
                lock.release()
        t = threading.Thread(target=inner)
        t.setDaemon(True)
        t.start()
        return t

    def run(self):
        _user = self.redis.keys()
        thread_lis = [self.login(user,self.users[user]) for user in self.users if user not in _user]
        if len(thread_lis):
            for t in thread_lis:
                t.join()
        self.run2()

    def run2(self):
        while 1:
            def inner(user,cookie):
                with sem:
                    headers = self.ret_headers(cookie)
                    All = pq(requests.get(cookice_url, headers=headers).text)
                    title = All('title').text()
                    if cookice_title not in title:
                        print('账号:%s有效'%user)
                    else:
                        print('账号:%s失效，重新获取' % user)
                        self.login(user,self.users[user])
            dic = self.redis.All_get()
            thread_lis = []
            for user in dic:
                t = threading.Thread(target=inner,args=(user,dic[user]))
                t.setDaemon(True)
                t.start()
                thread_lis.append(t)
            if len(thread_lis):
                for t in thread_lis:
                    t.join()
            time.sleep(cookice_sleep)
