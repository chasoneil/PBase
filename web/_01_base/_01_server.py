

# python 中自带的 wsgi 模块
from wsgiref.simple_server import make_server

from _01_hello import *

def start():

    # 创建服务
    httpd = make_server('', 8000, path_info)
    print('Service 8000 started...')

    # 开始监听http请求
    httpd.serve_forever()

if __name__ == '__main__':
    start()


