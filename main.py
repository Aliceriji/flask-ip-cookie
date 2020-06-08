import os,sys
sys.path.append(os.getcwd())
from app import app
from static.pro1 import *
from bin.api_config import run
from multiprocessing import Process
from bin.login_cookie import LOGIN

if __name__ == '__main__':
    r_login = LOGIN()
    Process(target=r_login.run).start()
    Process(target=run,).start()
    app.run(host='0.0.0.0',port=port)
