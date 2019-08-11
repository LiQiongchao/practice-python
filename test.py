import requests ;
import sys
from flask import json,Flask,make_response;
import time
app = Flask(__name__)
import hashlib
import sys
from datetime import datetime
from gevent.queue import Queue
import gevent
from cloghandler import ConcurrentRotatingFileHandler
import logging
import os
LOGLEVEL='DEBUG'

def f_log_concurrent(log_file):
    LEVELS = { 'debug':logging.DEBUG,'info':logging.INFO,'error':logging.ERROR}
    log = logging.getLogger()
    level=LEVELS.get(LOGLEVEL,logging.NOTSET)

    # Use an absolute path to prevent file rotation trouble.
    logfile = os.path.abspath(log_file)
    # Rotate log after reaching 1G, keep 60 old copies.
    rotateHandler = ConcurrentRotatingFileHandler(logfile, "a", 1024*1024*1024, 60,encoding="utf-8")
    fm=logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s","%Y-%m-%d %H:%M:%S",)
    rotateHandler.setFormatter(fm)
    log.addHandler(rotateHandler)
    log.setLevel(level)
    return log

def CheckSID(dict1, secret):
    if isinstance(dict1, dict):
        list1 = sorted(dict1.items(),key=lambda x:x[0])
        str=[]

        for list_item in iter(list1):
            if list_item[0]!='sid'and list_item[0]!='sign':                    # and list_item[0]!='rsvd':
                if list_item[1] is None:
                    continue
                str.append(list_item[0])
                str.append(list_item[1])

        str=(''.join(str))
    else:
        str=dict1
    str=(''.join((secret,str)))
    # print(str)
    a2md5 = hashlib.md5()
    a2md5.update(str.encode('utf-8'))
    a2md5_Digest = a2md5.hexdigest()
    a2md5value=a2md5_Digest.upper()
    return a2md5value


ts=datetime.now().strftime('%Y%m%d%H%M%S%f')[:17]
subts=datetime.now().strftime('%Y%m%d%H%M%S')
tasks =  Queue()

p=sys.argv[1]
other=int(p)
a=other+1
s = requests.Session()
b=time.time()
# appkey=''
# appsecret=''
appkey=''
appsecret=''

def worker(n):
    while  not tasks.empty():
        task = tasks.get()
        print('Worker %s got task %s' %  (n, task))
        print(a+task,other+task)

        value={"telX":'',
                "expiration":"1800",
                "requestId":str(a+task),
                "callrestrict":"1",
                "calldisplayshow":"1",
                "calldisplay":"0,0",
                "callrecording":"1",
                "subts":subts,
		"areacode":"029",
                "telA":str(a+task),
                "anucode":"218,218,218",
                "telB":str(other+task)}

        values={"telX":'',
                "expiration":"1800",
                "requestId":str(a+task),
                "extra":{"callrestrict":"1",
                         "calldisplayshow":"1",
                         "calldisplay":"0,0",
                         "callrecording":"1"},
                "subts":subts,
		"areacode":"029",
                "telA":str(a+task),
                "anucode":"218,218,218",
                "telB":str(other+task)}
        
        temp_d={'appkey':appkey,'ts':ts}
        temp_dict=value
        temp_dict.update(temp_d)
        msgdgt=CheckSID(temp_dict,appsecret)
        temp_dict.update({'msgdgt':msgdgt})
        headers = {'Content-Type': 'application/json','charset':'gbk'}
        headers.update(temp_dict)
        logging.info(values)
        b=time.time()
        # r = s.post("http://39.106.102.219:9110/v2/axb/mode102",json.dumps(values),headers=headers)
        r = s.post("",json.dumps(values),headers=headers)
        logging.info(r.json())
        e=time.time()
        logging.info(e-b)
        gevent.sleep(0)
    logging.info('Quitting time!')

def boss():
    for i in range(1,100):
        tasks.put_nowait(i)

gevent.spawn(boss).join()

f_log_concurrent('test.log')
gevent.joinall([
    gevent.spawn(worker, 'p1'),
    gevent.spawn(worker, 'p2'),
    gevent.spawn(worker, 'p3'),
    gevent.spawn(worker, 'p4'),
    gevent.spawn(worker, 'p5'),
    gevent.spawn(worker, 'p6'),
    gevent.spawn(worker, 'p7'),
    gevent.spawn(worker, 'p8'),
    gevent.spawn(worker, 'p9'),
    gevent.spawn(worker, 'p10'),
    gevent.spawn(worker, 'p11'),
    gevent.spawn(worker, 'p12'),
    gevent.spawn(worker, 'p13'),
    gevent.spawn(worker, 'p14'),
    gevent.spawn(worker, 'p15'),
    gevent.spawn(worker, 'p16'),
    gevent.spawn(worker, 'p17'),
    gevent.spawn(worker, 'p18'),
    gevent.spawn(worker, 'p19'),
    gevent.spawn(worker, 'p20'),
    gevent.spawn(worker, 'p21'),
    gevent.spawn(worker, 'p22'),
    gevent.spawn(worker, 'p23'),
    gevent.spawn(worker, 'p24'),
])



