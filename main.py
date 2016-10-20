import time
from httplib2 import Http
"""
http://202.207.7.180:8081/ClientWeb/pro/ajax/device.aspx?\
right=detail&classkind=8&room_id=100485887&name=1B%E5%8C%BA&open_start=730
&open_end=2200classkind&date=2016-10-20&start=13:40&end=14:40&fr_start=13:40
&fr_end=14:40&act=get_dev_coord&_nocache=1476941649431
"""

"""
GET http://202.207.7.180:8081/ClientWeb/pro/ajax/device.aspx?
right=detail&classkind=8&room_id=100485887&name=1B%E5%8C%BA&open_start=730
&open_end=2200classkind&date=2016-10-20&start=13:40&end=14:40&fr_start=14:30
&fr_end=14:40&act=get_rsv_sta&_nocache=1476944925867

"""
"""
http://202.207.7.180:8081/ClientWeb/pro/ajax/device.aspx?
right=detail&classkind=8&room_id=100485887&name=1B%E5%8C%BA&open_start=730
&open_end=2200classkind&date=2016-10-20&start=14:13&end=15:23&fr_start=13:23
&fr_end=14:33&act=get_dev_coord&_nocache=1476944590906
"""
"""
right=detail&classkind=8&room_id=100485887&name=1B%E5%8C%BA&open_start=730
&open_end=2200classkind&date=2016-10-20&start=14:05&end=14:25&fr_start=14:05
&fr_end=14:25&act=get_dev_coord&_nocache=1476944137372
"""


def get_lib_seats_info(room_id, name=''):
    # name = '1B%E5%8C%BA'
    http = Http()
    url = 'http://202.207.7.180:8081/ClientWeb/pro/ajax/device.aspx?'
    param = 'right=detail&classkind=8&room_id={{room_id}}' \
            '&name={{name}}&open_start=730&open_end=2200classkind&date={{date}}' \
            '&start={{start}}&end={{end}}&fr_start={{fr_start}}&fr_end={{fr_end}}&' \
            'act=get_rsv_sta&_nocache={{time}}'
    param = param.replace("{{room_id}}", str(room_id))
    param = param.replace("{{date}}", str(time.strftime("%Y-%m-%d")))
    param = param.replace("{{start}}", str(time.strftime("%H:%M", time.gmtime(time.time()-10*60 + 8 * 60 * 60))))
    param = param.replace("{{end}}", str(time.strftime("%H:%M", time.gmtime(time.time() + 60 * 60 + 8 * 60 * 60))))
    param = param.replace("{{fr_start}}", str(time.strftime("%H:%M", time.gmtime(time.time() - 60 * 60 + 8 * 60 * 60))))
    param = param.replace("{{fr_end}}", str(time.strftime("%H:%M", time.gmtime(time.time() + 10 * 60 + 8 * 60 * 60))))
    param = param.replace("{{time}}", str(int(time.time()*1000)))
    param = param.replace("{{name}}", str(name))
    url = url + param
    print(url)
    response, conetent = http.request(uri=url, method='GET')

    print(conetent.decode('utf-8'))



get_lib_seats_info("100485887")

"""
一个Python模块用于在内蒙古大学寻找一个人有没有在图书馆之中
"""
