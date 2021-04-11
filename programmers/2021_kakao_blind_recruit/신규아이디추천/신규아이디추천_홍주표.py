POSSIBLE = 'abcdefghijklmnopqrstuvwxyz0123456789-_.'

def solution(new_id):
    bb = ''
    for char in new_id.lower():
        if char in POSSIBLE:
            bb += char
    cc = ''
    for idx in range(len(bb) - 1):
        if bb[idx] == '.' and bb[idx + 1] == '.':
            continue
        cc += bb[idx]
    cc += bb[-1]
    dd = cc.strip('.')
    ee = dd if dd else 'a'
    if len(ee) > 15:
        ee = ee[:15]
    ff = ee.strip('.')
    while len(ff) <= 2:
        ff += ff[-1]
    return ff


# 정규식 쓴 사람의 코드
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
