import requests
import json
import re
import base64


def record(path):
    f = open('image.png', 'rb')
    ls_f = base64.b64encode(f.read())
    f.close()
    kw = {'access_token': '24.d554aefe26f270cb88251bff78fe76db.2592000.1623846948.282335-24190192'}
    headers = {
            "Content-Type": "application/x-www-form-urlencoded"}
    host = "https://aip.baidubce.com/rest/2.0/ocr/v1/general"
    body = {
            'image': ls_f}
    response = requests.post(host, params=kw, headers=headers, data=body)
    j = json.dumps(response.json())
    dics = json.loads(j).get('words_result')
    words = []
    for word in dics:
        words.append(word['words'])
    name = []
    for word in words:
        flag = re.match('B19', word)
        if flag:
                name.append(word)
                break
    flag0 = 1
    for word in words:

        flag = re.match('第', word)
        if flag0 == 0:
            name.append(word)
            break
        if flag:
            name.append(word)
            flag0 = 0
    name.append("你这什么玩意？")
    with open("students.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        # print(lines)
    with open("students.txt", "w", encoding="utf-8") as f_w:
        for line in lines:
            if name[0] in line:
                name[3] = "消息已经收到啦"
                strs = name[0] + name[1] + name[2] + ',' + name[3]
                f_w.write(strs)
            else:
                f_w.write(line)
    return name
