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
class Student:
    id = ''
    seat = ''
    name = ''

def send_request(room_id, name=''):
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
    # print(url)
    response, conetent = http.request(uri=url, method='GET')

    # print(conetent.decode('utf-8'))
    return conetent.decode('utf-8')

def get_seat_info_dict():

    list = []
    # 1B
    temp_list = analyze_result(send_request("100485887"))

    list.extend(temp_list)

    temp_list = analyze_result(send_request("100485889"))

    list.extend(temp_list)

    temp_list = analyze_result(send_request("100485891"))

    list.extend(temp_list)

    temp_list = analyze_result(send_request("100485893"))

    list.extend(temp_list)

    temp_list = analyze_result(send_request("100485895"))

    list.extend(temp_list)

    temp_list = analyze_result(send_request("100485897"))

    list.extend(temp_list)

    temp_list = analyze_result(send_request("100485899"))

    list.extend(temp_list)

    return list
def analyze_result(content):
    content = str(content).replace("null", "\"null\"")
    content = str(content).replace("false", "\"false\"")
    content = content.replace('true', "\"true\"")
    data = eval(content).get('data')
    students = []
    for element in data:
        if len(element.get('ts')) == 0 :
            continue
        if element.get('ts')[0].get('owner') == "null":
            name = element.get('ts')[0].get('owner')
            print(name)
            continue
        student = Student()
        student.id = element.get('id')
        student.name = element.get('ts')[0].get('owner')
        student.seat = element.get('labName') + " " + element.get('title')
        students.append(student)
    return students

"""
main
"""
for student in get_seat_info_dict():
    print("id:" + student.id)
    print("name:" + student.name)
    print("seat:" + student.seat)
    print('\n')
